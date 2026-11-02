#!/usr/bin/env python3
"""
Kill-First Desk: live PAPER trader for new Solana memecoins.

No wallet, no keys, no real trades. It reads live market data, makes the same
decisions the real bot would, and records what would have happened.

Workers (each one can stop a coin):
  Scouts     DexScreener new profiles + boosts, pump.fun newest coins
  Security   RugCheck report: mint/freeze authority, dev %, insiders, top holders,
             liquidity, past rugs   (plain code rules, same answer every time)
  Sell test  Jupiter buy quote, then sell quote: catches honeypots, sell taxes,
             and gives an honest fill price including exchange fees and impact
  Council    deterministic 0-100 score: momentum (heaviest), community, social
  Risk       2% bets, max open trades, daily loss limit
  Exits      -40% stop, sell 25% at +150%, 50% trailing stop on the rest,
             sell if the coin dies (no liquidity / no route)

To measure whether the council actually has an edge, a CONTROL wallet buys a
random sample of coins that passed security, ignoring the council score.
If the council's picks don't beat the control picks, the signal isn't real.

Run:   python paper_trader.py --minutes 345
Mock:  python paper_trader.py --mock --minutes 3 --poll 0.2   (offline test)
"""
import argparse, json, math, os, random, sys, time
from datetime import datetime, timezone

CFG = dict(
    start_usd=77.0,
    bet_pct=2.0,              # % of wallet per trade
    max_open=5,
    daily_loss_pct=40.0,      # stop buying for the UTC day after losing this much
    # security (fail closed: unknown = killed)
    max_dev_pct=10.0, max_insider_pct=25.0, max_top10_pct=35.0,
    min_liq_usd=5_000, min_vol_usd=40_000, max_h1_change=1e9,   # "already pumped" filter off: its coins doubled as often as our picks
    max_roundtrip_loss=15.0,  # % lost buying then instantly selling (tax + fees + impact)
    max_avg_trade_usd=2_000,  # few huge trades = likely fake volume
    # council
    min_score=70, min_tx_m5=0,
    # exits
    stop_pct=40.0, target_pct=150.0, sell_part=0.25, trail_pct=50.0,
    dead_minutes=10, dev_watch_sec=60, min_tx_h1=5,   # fewer trades than this in the last hour = dead coin
    # costs not in the Jupiter quote
    priority_fee_usd=0.05, jito_tip_usd=0.02,
    # control group
    control_prob=0.3,
    # follow-up on killed coins
    followup_minutes=60, pumped_x=2.0, followup_cap=400,
)
SOL = "So11111111111111111111111111111111111111112"
USDC = "EPjFWdd5AufqSSqLM2bmQ9wXDG7Bpq1yYZ9KTDj2Dt1v"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
REPORT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "REPORT.md")
LAB_SNAPS = (5, 15, 30, 60, 120, 240)   # minutes after first check when the lab records each coin's price
REPORT_RETRY_MIN = (2, 5, 10, 20)   # minutes to wait before asking RugCheck again about a coin it doesn't know yet
RETRY_MIN = (3, 10, 30)   # minutes after first sight to look at a young coin again
QUIET = {"No market yet", "Volume too low"}   # counted, not logged one by one
UA = {"User-Agent": "kill-first-desk-paper/1.0", "Accept": "application/json"}

import re
def safe(url): return re.sub(r"(api-key=)[^&]+", r"\1***", url)
def now(): return time.time()
def debug(msg):
    try:
        with open(os.path.join(DATA, "api-debug.txt"), "a") as fh: fh.write(iso() + " " + msg + "\n")
    except Exception: pass
def iso(ts=None): return datetime.fromtimestamp(ts or now(), timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
def day(ts=None): return datetime.fromtimestamp(ts or now(), timezone.utc).strftime("%Y-%m-%d")
def live(kind, d):
    """One readable line per event, for the live log on GitHub."""
    t = d.get("t", iso())[11:19]; sym = str(d.get("sym") or "")[:12]
    if kind == "buy":
        line = f"{t}  BUY   {sym:<12} ${d.get('usd', 0):.2f}  [{d.get('wallet')}]  score {d.get('score')}  round trip {d.get('roundtrip_loss')}%"
    elif kind == "exit":
        line = f"{t}  SELL  {sym:<12} {'+' if d.get('pnl', 0) > 0 else ''}${d.get('pnl', 0):.2f}  [{d.get('wallet')}]  {d.get('why')}  after {d.get('held_min')} min"
    elif kind == "partial":
        line = f"{t}  PART  {sym:<12} ${d.get('usd', 0):.2f}  [{d.get('wallet')}]  {d.get('why')}"
    elif kind == "kill":
        extra = f"  score {d['score']}" if "score" in d else ""
        line = f"{t}  skip  {sym:<12} {d.get('reason')}{extra}"
    elif kind == "missed":
        line = f"{t}  MISS  {str(d.get('mint',''))[:8]:<12} killed for '{d.get('reason')}' but went {d.get('x')}x"
    else:
        return
    if d.get("reason") == "Too many open trades": return   # too noisy to show live
    try: print(line, flush=True)
    except Exception: pass

def clip(x, a=0.0, b=1.0): return max(a, min(b, x))
def fnum(x, d=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


# ------------------------------------------------------------------ HTTP layer
class Net:
    def __init__(self):
        import requests
        self.s = requests.Session(); self.s.headers.update(UA)
        self.last = {}; self.errors = {}; self.shown = set()
    def get(self, url, gap=0.25, timeout=12, headers=None):
        host = url.split("/")[2]
        wait = self.last.get(host, 0) + gap - now()
        if wait > 0: time.sleep(wait)
        self.last[host] = now()
        key = url.split("?")[0].rsplit("/", 1)[0]
        try:
            r = self.s.get(url, timeout=timeout, headers=headers)
            if (key, r.status_code) not in self.shown:   # show each endpoint's first answer once, for debugging
                self.shown.add((key, r.status_code))
                msg = f"[api] {r.status_code} {safe(url)[:90]} :: {r.text[:220]!r}"; print(msg, flush=True); debug(msg)
            if r.status_code == 429:
                self.errors[host + " (rate limited)"] = self.errors.get(host + " (rate limited)", 0) + 1
                time.sleep(5); return None
            if not r.ok:
                self.errors[f"{host} ({r.status_code})"] = self.errors.get(f"{host} ({r.status_code})", 0) + 1; return None
            return r.json()
        except Exception as e:
            k = f"{host} ({type(e).__name__})"
            if k not in self.shown:
                self.shown.add(k); msg = f"[api] error {safe(url)[:90]} :: {safe(repr(e))}"[:300]; print(msg, flush=True); debug(msg)
            self.errors[k] = self.errors.get(k, 0) + 1; return None


    def post(self, url, body, gap=0.15, timeout=15):
        host = url.split("/")[2]
        wait = self.last.get(host, 0) + gap - now()
        if wait > 0: time.sleep(wait)
        self.last[host] = now()
        tag = f"{host} {body.get('method')}"
        try:
            r = self.s.post(url, json=body, timeout=timeout)
            if (tag, r.status_code) not in self.shown:
                self.shown.add((tag, r.status_code))
                msg = f"[api] {r.status_code} {tag} :: {r.text[:200]!r}"; print(msg, flush=True); debug(msg)
            if not r.ok:
                self.errors[f"{host} ({r.status_code})"] = self.errors.get(f"{host} ({r.status_code})", 0) + 1; return None
            d = r.json()
            if d.get("error"):
                err = d["error"]; code = err.get("code") if isinstance(err, dict) else err
                k = f"{host} (rpc error {code})"
                if k not in self.shown:
                    self.shown.add(k); msg = f"[api] rpc error {tag} :: {str(err)[:200]}"; print(msg, flush=True); debug(msg)
                self.errors[k] = self.errors.get(k, 0) + 1; return None
            return d.get("result")
        except Exception as e:
            self.errors[f"{host} ({type(e).__name__})"] = self.errors.get(f"{host} ({type(e).__name__})", 0) + 1; return None


class Helius:
    """Watches the coin creator's wallet. Needs a free HELIUS_API_KEY."""
    def __init__(self, net, key):
        self.n = net; self.url = f"https://mainnet.helius-rpc.com/?api-key={key}"; self.calls = 0
    def rpc(self, method, params):
        self.calls += 1
        return self.n.post(self.url, {"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
    def recent(self, wallet, limit=10):
        return self.rpc("getSignaturesForAddress", [wallet, {"limit": limit}]) or []
    def sold(self, wallet, mint, sig):
        """True if this transaction lowered the wallet's balance of the coin."""
        tx = self.rpc("getTransaction", [sig, {"maxSupportedTransactionVersion": 1, "encoding": "jsonParsed", "commitment": "confirmed"}])
        meta = (tx or {}).get("meta") or {}
        def bal(lst):
            return sum(fnum(((b.get("uiTokenAmount") or {}).get("uiAmount")), 0) or 0
                       for b in lst or [] if b.get("mint") == mint and b.get("owner") == wallet)
        return bal(meta.get("postTokenBalances")) < bal(meta.get("preTokenBalances")) - 1e-9
    def dev_sold_since(self, wallet, mint, since=0, max_tx=8):
        """Look at the creator's latest transactions. Returns (sold?, newest blockTime seen)."""
        sigs = self.recent(wallet, limit=max_tx)
        newest = max([x.get("blockTime") or 0 for x in sigs] or [since])
        for x in sigs:
            if (x.get("blockTime") or 0) <= since or x.get("err"): continue
            if self.sold(wallet, mint, x["signature"]): return True, newest
        return False, newest


class API:
    def __init__(self, net): self.n = net
    # scouts
    def new_profiles(self):
        out = []
        for u in ("https://api.dexscreener.com/token-profiles/latest/v1",
                  "https://api.dexscreener.com/token-boosts/latest/v1"):
            for p in self.n.get(u, gap=1.1) or []:
                if p.get("chainId") == "solana" and p.get("tokenAddress"):
                    out.append(("dexscreener", p["tokenAddress"], p))
        return out
    def pump_newest(self):
        d = self.n.get("https://frontend-api-v3.pump.fun/coins?offset=0&limit=50&sort=created_timestamp&order=DESC&includeNsfw=false", gap=2)
        return [("pumpfun", c["mint"], c) for c in (d or []) if isinstance(c, dict) and c.get("mint")]
    # market data, up to 30 mints per call
    def pairs(self, mints):
        res = {}
        for i in range(0, len(mints), 30):
            chunk = mints[i:i + 30]
            d = self.n.get("https://api.dexscreener.com/tokens/v1/solana/" + ",".join(chunk), gap=0.25)
            for p in d or []:
                a = (p.get("baseToken") or {}).get("address")
                if not a: continue
                liq = fnum((p.get("liquidity") or {}).get("usd"), 0) or 0
                if a not in res or liq > (fnum((res[a].get("liquidity") or {}).get("usd"), 0) or 0):
                    res[a] = p
        return res
    def rugcheck(self, mint):
        return self.n.get(f"https://api.rugcheck.xyz/v1/tokens/{mint}/report", gap=1.2, timeout=20)
    jup_fails = 0
    def quote(self, in_mint, out_mint, amount):
        if amount <= 0: return None
        q = (f"/swap/v1/quote?inputMint={in_mint}&outputMint={out_mint}"
             f"&amount={int(amount)}&slippageBps=1500&restrictIntermediateTokens=true")
        key = os.environ.get("JUP_API_KEY")
        d = self.n.get("https://api.jup.ag" + q, gap=1.1, headers={"x-api-key": key}) if key else None
        if not d or "outAmount" not in d:
            d = self.n.get("https://lite-api.jup.ag" + q, gap=1.1)
        if not d or "outAmount" not in d:
            self.jup_fails += 1; return None
        self.jup_fails = 0
        return int(d["outAmount"])
    def jup_down(self): return self.jup_fails >= 5
    def sol_usd(self):
        d = self.n.get("https://api.dexscreener.com/tokens/v1/solana/" + SOL, gap=0.25) or []
        best = max((p for p in d if (p.get("baseToken") or {}).get("address") == SOL), default=None,
                   key=lambda p: fnum((p.get("liquidity") or {}).get("usd"), 0) or 0)
        if best: return fnum(best.get("priceUsd"))
        out = None if self.jup_down() else self.quote(SOL, USDC, 10**9)
        return out / 1e6 if out else None


# ------------------------------------------------------------------ the workers
def security(rep, pair, cfg, min_vol=None):
    """Plain-code rules. Returns (ok, reason, facts). Unknown = killed."""
    if not rep: return False, "No security report", {}
    f = {}
    if rep.get("rugged"): return False, "Already rugged", f
    if rep.get("mintAuthority"): return False, "Mint authority active", f
    if rep.get("freezeAuthority"): return False, "Freeze authority active", f
    known = rep.get("knownAccounts") or {}
    def is_pool(addr):
        k = known.get(addr) or {}
        return str(k.get("type", "")).upper() in ("AMM", "LOCKER", "POOL") or "curve" in str(k.get("name", "")).lower()
    holders = [h for h in rep.get("topHolders") or [] if not is_pool(h.get("owner")) and not is_pool(h.get("address"))]
    creator = rep.get("creator")
    dev = sum(fnum(h.get("pct"), 0) or 0 for h in holders if creator and h.get("owner") == creator)
    insiders = sum(fnum(h.get("pct"), 0) or 0 for h in holders if h.get("insider"))
    top10 = sum(fnum(h.get("pct"), 0) or 0 for h in holders[:10])
    f.update(dev=round(dev, 1), insiders=round(insiders, 1), top10=round(top10, 1))
    if not holders: return False, "No holder data", f
    if dev > cfg["max_dev_pct"]: return False, "Dev holds too much", f
    if insiders > cfg["max_insider_pct"]: return False, "Insider / bundled supply", f
    if top10 > cfg["max_top10_pct"]: return False, "Top 10 holders own too much", f
    for r in rep.get("risks") or []:
        name = str(r.get("name", "")).lower()
        if r.get("level") == "danger" and ("rug" in name or "copycat" in name or "freeze" in name or "mint" in name):
            return False, "Danger flag: " + str(r.get("name"))[:40], f
    dex = (pair or {}).get("dexId", "")
    on_curve = dex in ("pumpfun", "pump", "moonshot", "launchlab", "meteora-dbc") or "curve" in dex
    if not on_curve:
        locked = max([fnum(((m.get("lp") or {}).get("lpLockedPct")), 0) or 0 for m in rep.get("markets") or []] or [0])
        f["lp_locked"] = round(locked)
        if locked < 90: return False, "Liquidity not locked or burned", f
    if not pair: return False, "No market data", f
    liq = fnum((pair.get("liquidity") or {}).get("usd"), 0) or 0
    vol = fnum((pair.get("volume") or {}).get("h24"), 0) or 0
    h1 = fnum((pair.get("priceChange") or {}).get("h1"), 0) or 0
    tx = (pair.get("txns") or {}).get("h1") or {}
    n_tx = (tx.get("buys") or 0) + (tx.get("sells") or 0)
    vol_h1 = fnum((pair.get("volume") or {}).get("h1"), 0) or 0
    f.update(liq=round(liq), vol=round(vol), h1=round(h1), tx_h1=n_tx)
    if not on_curve and liq < cfg["min_liq_usd"]: return False, "Liquidity too low", f
    if vol < (cfg["min_vol_usd"] if min_vol is None else min_vol): return False, "Volume too low", f
    if h1 >= cfg["max_h1_change"]: return False, "Already pumped this hour", f
    if n_tx and vol_h1 / n_tx > cfg["max_avg_trade_usd"] and n_tx < 50: return False, "Few huge trades (fake volume?)", f
    return True, "", f


def est_impact(usd, pair):
    """Price impact estimate when no live quote: bet size against pool depth."""
    liq = fnum((pair.get("liquidity") or {}).get("usd"), 0) or 0
    if liq <= 0: liq = 0.25 * (fnum(pair.get("marketCap"), 0) or fnum(pair.get("fdv"), 0) or 0)
    return 0.5 if liq <= 0 else min(0.5, usd / liq)

EXCHANGE_FEE = 0.0125

def features(pair, rep, meta=None):
    """Everything we know about a coin at decision time, logged so the lab can learn from it."""
    tx = pair.get("txns") or {}; vol = pair.get("volume") or {}; ch = pair.get("priceChange") or {}
    def bs(w):
        t = tx.get(w) or {}; return (t.get("buys") or 0), (t.get("sells") or 0)
    b5, s5 = bs("m5"); b1, s1 = bs("h1"); b6, s6 = bs("h6")
    born = fnum(pair.get("pairCreatedAt"))
    age = (now() - born / 1000) / 60 if born else None
    holders = fnum((rep or {}).get("totalHolders"), 0) or 0
    info = pair.get("info") or {}; m = meta if isinstance(meta, dict) else {}
    return dict(
        tx_m5=b5 + s5, ratio_m5=round(b5 / (b5 + s5), 3) if b5 + s5 else None,
        tx_h1=b1 + s1, ratio_h1=round(b1 / (b1 + s1), 3) if b1 + s1 else None, tx_h6=b6 + s6,
        accel=round((b5 + s5) * 12 / (b1 + s1), 2) if b1 + s1 else None,
        vol_m5=round(fnum(vol.get("m5"), 0) or 0), vol_h1=round(fnum(vol.get("h1"), 0) or 0), vol_h24=round(fnum(vol.get("h24"), 0) or 0),
        ch_m5=fnum(ch.get("m5")), ch_h1=fnum(ch.get("h1")), ch_h6=fnum(ch.get("h6")),
        liq=round(fnum((pair.get("liquidity") or {}).get("usd"), 0) or 0), mcap=round(fnum(pair.get("marketCap"), 0) or fnum(pair.get("fdv"), 0) or 0),
        age_min=round(age, 1) if age is not None else None, holders=int(holders),
        holders_per_min=round(holders / max(age, 1), 2) if age else None,
        dex=pair.get("dexId"), socials=len(info.get("socials") or []) + len(info.get("websites") or []) + sum(1 for k in ("twitter", "telegram", "website") if m.get(k)),
        boosts=(pair.get("boosts") or {}).get("active") or 0,
        avg_trade=round((fnum(vol.get("h1"), 0) or 0) / (b1 + s1), 1) if b1 + s1 else None)


def v3_rule(f):
    """Council v3: the one pattern that held up across 62,024 lab coins, judged on first-sight numbers.
    Buys are 75%+ of the last 5 minutes of trades, price is up over the last hour,
    market cap $10k-$300k, and the coin is under an hour old. 28% of matching coins doubled vs 1.5% overall."""
    g = lambda k, d: f.get(k) if f.get(k) is not None else d
    return (g("ratio_m5", 0) >= 0.75 and g("ch_h1", -1) > 0 and 1e4 <= g("mcap", 0) < 3e5 and g("age_min", 999) < 60)


def council(pair, rep, src):
    """Version 2. Deterministic: same coin, same data -> same score.
    Built from the first live run, where 1-hour numbers couldn't tell rising coins from fading ones:
    momentum now comes from the last 5 minutes and whether trading is speeding up."""
    f = features(pair, rep, src)
    r5 = f["ratio_m5"] or 0; acc = f["accel"] or 0; t5 = f["tx_m5"]
    mo = 100 * (0.4 * clip((r5 - 0.5) / 0.2) + 0.3 * clip((acc - 0.5) / 1.0) + 0.3 * clip(math.log10(max(t5, 1)) / 2.5))
    hpm = f["holders_per_min"]
    cm = 100 * (0.5 * clip(math.log10(max(f["holders"], 1)) / 3) + 0.5 * (clip(math.log10(max(hpm * 10, 1)) / 2) if hpm is not None else 0.5))
    so = [30, 55, 75, 90][min(3, f["socials"])]
    score = round(0.7 * mo + 0.2 * cm + 0.1 * so)
    return score, dict(momentum=round(mo), social=so, community=round(cm), **f)


def council_v1(pair, rep, src):
    """First version, kept for comparison."""
    tx = (pair.get("txns") or {}).get("h1") or {}
    b, s = tx.get("buys") or 0, tx.get("sells") or 0
    ratio = b / (b + s) if b + s else 0
    mo = 100 * (0.5 * clip((ratio - 0.45) / 0.25) + 0.5 * clip(math.log10(max(b + s, 1)) / 3))
    socials = (pair.get("info") or {}).get("socials") or []
    sites = (pair.get("info") or {}).get("websites") or []
    meta = src if isinstance(src, dict) else {}
    n_soc = len(socials) + len(sites) + sum(1 for k in ("twitter", "telegram", "website") if meta.get(k))
    so = [30, 55, 75, 90][min(3, n_soc)]
    holders = fnum((rep or {}).get("totalHolders"), 0) or 0
    born = fnum(pair.get("pairCreatedAt"))
    age_min = max(1.0, (now() - born / 1000) / 60) if born else None
    per_min = holders / age_min if age_min else None
    size_score = clip(math.log10(max(holders, 1)) / 3)
    growth_score = clip(math.log10(max(per_min * 10, 1)) / 2) if per_min is not None else size_score
    cm = 100 * (0.5 * size_score + 0.5 * growth_score)
    score = round(0.5 * mo + 0.2 * so + 0.3 * cm)
    return score, dict(momentum=round(mo), social=so, community=round(cm), holders=int(holders), buy_ratio=round(ratio, 2),
                       holders_per_min=round(per_min, 2) if per_min is not None else None)


# ------------------------------------------------------------------ wallets
class Wallet:
    def __init__(self, name, d=None):
        self.name = name
        d = d or {}
        self.cash = d.get("cash", CFG["start_usd"]); self.start = d.get("start", CFG["start_usd"])
        self.open = d.get("open", {}); self.closed = d.get("closed", [])
        self.day = d.get("day", day()); self.day_start = d.get("day_start", self.cash)
    def dump(self): return dict(cash=self.cash, start=self.start, open=self.open, closed=self.closed[-2000:], day=self.day, day_start=self.day_start)
    def equity(self): return self.cash + sum(p["cost"] for p in self.open.values())
    def value(self):
        """Marked to the latest price, ignoring exit costs."""
        v = self.cash
        for p in self.open.values():
            share = p["left"] / p["tokens"] if p["tokens"] else 0
            move = (p.get("mark") or p["entry"]) / p["entry"] if p["entry"] else 1
            v += share * p["cost"] * move
        return v
    def roll_day(self):
        if self.day != day(): self.day = day(); self.day_start = self.equity()
    def blocked(self):
        self.roll_day()
        if len(self.open) >= CFG["max_open"]: return "Too many open trades"
        if self.equity() <= self.day_start * (1 - CFG["daily_loss_pct"] / 100): return "Daily loss limit hit"
        if self.cash < 0.5: return "Out of cash"
        return None


class Desk:
    def __init__(self, api, cfg, state=None):
        self.api, self.cfg = api, cfg
        st = state or {}
        self.w = {"council": Wallet("council", st.get("council")), "control": Wallet("control", st.get("control"))}
        self.seen = dict.fromkeys(st.get("seen", []))
        self.follow = st.get("follow", [])
        self.retry = st.get("retry", [])
        self.report_tries = st.get("report_tries", {})   # young coins rechecked later: no market yet / volume still low
        self.stats = st.get("stats", {"found": 0, "kills": {}, "kills_pumped": {}, "kills_checked": {}, "scores": []})
        self.sol = None; self.sol_t = 0
        self.helius = None
        lp = os.path.join(DATA, "lab-pending.json")
        pend = json.load(open(lp)) if os.path.exists(lp) else (st.get("lab") or {})
        self.lab = {m: {**e, "snaps": {float(k) if "." in str(k) else int(k): v for k, v in e["snaps"].items()}} for m, e in pend.items()}
        self.last_manage = 0
        os.makedirs(DATA, exist_ok=True)

    # logging
    def log(self, kind, **kw):
        kw.update(t=iso(), kind=kind)
        live(kind, kw)
        with open(os.path.join(DATA, f"log-{day()}.jsonl"), "a") as fh:
            fh.write(json.dumps(kw, separators=(",", ":")) + "\n")

    # ---- lab: follow every coin that reached the security check, bought or not
    def lab_add(self, mint, sym, pair, rep, meta, facts):
        price = fnum(pair.get("priceUsd"))
        if mint in self.lab:
            if facts and not self.lab[mint]["sec"]: self.lab[mint]["sec"] = dict(facts)
            if rep and not self.lab[mint]["f"].get("holders"): self.lab[mint]["f"]["holders"] = int(fnum(rep.get("totalHolders"), 0) or 0)
            return
        if not price or len(self.lab) > 12000: return
        self.lab[mint] = dict(mint=mint, sym=sym, t0=now(), p0=price, hi=price, lo=price, snaps={}, verdict="?",
                              f=features(pair, rep, meta), sec=dict(facts))
    def lab_mark(self, mint, verdict, score=None):
        e = self.lab.get(mint)
        if e and e["verdict"] in ("?", "passed"):
            e["verdict"] = verdict
            if score is not None: e["score"] = score
    def lab_update(self):
        due = [e for e in self.lab.values() if any(m not in e["snaps"] and now() - e["t0"] >= m * 60 for m in LAB_SNAPS)]
        if not due: return
        due = due[:900]
        pairs = self.api.pairs([e["mint"] for e in due])
        for e in due:
            pair = pairs.get(e["mint"]); price = fnum((pair or {}).get("priceUsd"))
            tx1 = ((pair or {}).get("txns") or {}).get("h1") or {}
            alive = price and (tx1.get("buys") or 0) + (tx1.get("sells") or 0) >= self.cfg["min_tx_h1"]
            for m in LAB_SNAPS:
                if m not in e["snaps"] and now() - e["t0"] >= m * 60:
                    e["snaps"][m] = round(price / e["p0"], 3) if alive else 0
            if alive:
                e["hi"] = max(e["hi"], price); e["lo"] = min(e["lo"], price)
        for mint in [m for m, e in self.lab.items() if len(e["snaps"]) == len(LAB_SNAPS)]:
            e = self.lab.pop(mint)
            e["max_x"] = round(e["hi"] / e["p0"], 3); e["min_x"] = round(e["lo"] / e["p0"], 3)
            e["snaps"] = {str(k): v for k, v in e["snaps"].items()}
            for k in ("hi", "lo"): e.pop(k)
            with open(os.path.join(DATA, "lab.jsonl"), "a") as fh: fh.write(json.dumps(e, separators=(",", ":")) + "\n")
            self.stats["lab_done"] = self.stats.get("lab_done", 0) + 1

    def kill(self, mint, sym, reason, price=None, **kw):
        self.lab_mark(mint, reason)
        k = self.stats["kills"]; k[reason] = k.get(reason, 0) + 1
        if reason not in QUIET: self.log("kill", mint=mint, sym=sym, reason=reason, **kw)
        if price and len(self.follow) < self.cfg["followup_cap"]:
            self.follow.append(dict(mint=mint, reason=reason, price=price, t=now()))

    def sol_price(self):
        if not self.sol or now() - self.sol_t > 300:
            p = self.api.sol_usd()
            if p: self.sol, self.sol_t = p, now()
        return self.sol

    # one scouting pass
    def scout(self):
        cands = []
        for src in (self.api.new_profiles(), self.api.pump_newest()):
            for name, mint, meta in src:
                if mint not in self.seen:
                    self.seen[mint] = None; cands.append((name, mint, meta))
        self.stats["found"] += len(cands)
        jobs = [(n, m, meta, 0) for n, m, meta in cands]
        due = [r for r in self.retry if r["due"] <= now()][:40]
        if due:
            ids = {id(r) for r in due}; self.retry = [r for r in self.retry if id(r) not in ids]
            jobs += [(r["src"], r["mint"], r["meta"], r["n"]) for r in due]
        if not jobs: return
        pairs = self.api.pairs([j[1] for j in jobs])
        for name, mint, meta, n in jobs:
            if now() - self.last_manage > 20: self.manage()
            self.attempt = n
            r = self.judge(name, mint, meta, pairs.get(mint))
            if r == "RETRY" and self.last_reason == "No security report":
                k = self.report_tries.get(mint, 0); self.report_tries[mint] = k + 1
                small = {kk: meta.get(kk) for kk in ("symbol", "twitter", "telegram", "website")} if isinstance(meta, dict) else {}
                self.retry.append(dict(src=name, mint=mint, meta=small, n=n, due=now() + REPORT_RETRY_MIN[k] * 60))
                self.stats["report_retries"] = self.stats.get("report_retries", 0) + 1
            elif r == "RETRY":
                if n < len(RETRY_MIN) and len(self.retry) < 3000:
                    small = {k: meta.get(k) for k in ("symbol", "twitter", "telegram", "website")} if isinstance(meta, dict) else {}
                    self.retry.append(dict(src=name, mint=mint, meta=small, n=n + 1, due=now() + RETRY_MIN[n] * 60))
                else:
                    self.kill(mint, self.last_sym, self.last_reason, self.last_price)

    def judge(self, src, mint, meta, pair):
        sym = ((pair or {}).get("baseToken") or {}).get("symbol") or (meta.get("symbol") if isinstance(meta, dict) else None) or mint[:6]
        price = fnum((pair or {}).get("priceUsd"))
        self.last_sym, self.last_price = sym, price
        if not pair:
            self.last_reason = "No market yet"; return "RETRY"
        self.lab_add(mint, sym, pair, None, meta, {})
        v3 = v3_rule(features(pair, None, meta))
        if v3: self.stats["v3_seen"] = self.stats.get("v3_seen", 0) + 1
        vol = fnum((pair.get("volume") or {}).get("h24"), 0) or 0
        if v3:
            pass   # the signal is strongest right now: skip the volume wait and check it immediately
        elif vol < self.cfg["min_vol_usd"] * 0.25:    # cheap pre-filter before the slow security calls
            self.last_reason = "Volume too low"; return "RETRY"
        elif vol < self.cfg["min_vol_usd"] and getattr(self, "attempt", 0) < len(RETRY_MIN):
            self.last_reason = "Volume too low"; return "RETRY"   # young coin: look again before running security
        rep = self.api.rugcheck(mint)
        if not rep and self.report_tries.get(mint, 0) < len(REPORT_RETRY_MIN):
            # brand-new coins often aren't in RugCheck yet: look again shortly instead of dropping them
            self.lab_add(mint, sym, pair, None, meta, {})
            self.last_reason = "No security report"; return "RETRY"
        ok, why, facts = security(rep, pair, self.cfg, min_vol=0 if v3 else None)
        self.lab_add(mint, sym, pair, rep, meta, facts)
        if not ok:
            self.lab_mark(mint, why)
            return self.kill(mint, sym, why, price, **facts)
        sol = self.sol_price()
        if not sol:
            return self.kill(mint, sym, "No SOL price")
        bet_usd = max(1.0, self.w["council"].equity() * self.cfg["bet_pct"] / 100)
        if self.api.jup_down():
            # no live quotes: lean on RugCheck flags for taxes / honeypots and estimate the round trip
            for r in rep.get("risks") or []:
                nm = (str(r.get("name", "")) + " " + str(r.get("description", ""))).lower()
                if any(w in nm for w in ("transfer fee", "tax", "honeypot", "non-transferable", "permanent delegate")):
                    return self.kill(mint, sym, "Tax or transfer restriction flag", price, **facts)
            rt = 100 * (2 * EXCHANGE_FEE + 2 * est_impact(bet_usd, pair))
            facts["fills"] = "estimated"
        else:
            lamports = int(bet_usd / sol * 1e9)
            got = self.api.quote(SOL, mint, lamports)
            back = self.api.quote(mint, SOL, got) if got else None
            if not got or not back:
                return self.kill(mint, sym, "Sell test failed (honeypot or no route)", price, **facts)
            rt = 100 * (1 - back / lamports)
            facts["fills"] = "jupiter"
        facts["roundtrip_loss"] = round(rt, 1)
        if rt > self.cfg["max_roundtrip_loss"]:
            return self.kill(mint, sym, "Sell test: tax or fees too high", price, **facts)
        score, parts = council(pair, rep, meta)
        facts.update(score=score, **parts)
        self.lab_mark(mint, "passed", score)
        if parts["tx_m5"] < self.cfg["min_tx_m5"]:
            return self.kill(mint, sym, "Fading: few trades in last 5 min", price, **facts)
        self.stats["scores"].append(score); self.stats["scores"] = self.stats["scores"][-5000:]
        took = False
        ctrl = random.random() < self.cfg["control_prob"]
        creator = (rep or {}).get("creator")
        facts["creator"] = creator
        facts["v3"] = v3_rule(parts)   # recheck on fresh numbers at decision time
        if (facts["v3"] or ctrl) and self.helius and creator:
            sold, last = self.helius.dev_sold_since(creator, mint)
            facts["dev_checked"] = last
            if sold:
                return self.kill(mint, sym, "Dev wallet already selling", price, **facts)
        if facts["v3"]:
            took = self.buy("council", mint, sym, pair, facts, sol)
        else:
            self.kill(mint, sym, "Doesn't match the v3 pattern", price, **facts)
        if ctrl:
            self.buy("control", mint, sym, pair, facts, sol)
        return took

    def buy(self, wname, mint, sym, pair, facts, sol):
        w = self.w[wname]
        if mint in w.open: return False
        b = w.blocked()
        if b:
            if wname == "council": self.kill(mint, sym, b, fnum(pair.get("priceUsd")), **facts)
            return False
        usd = min(w.cash, max(1.0, w.equity() * self.cfg["bet_pct"] / 100))
        price = fnum(pair.get("priceUsd"), 0)
        if facts.get("fills") == "estimated":
            if not price: return False
            tokens = usd * (1 - EXCHANGE_FEE - est_impact(usd, pair)) / price * 1e6   # paper units, 6 decimals
            mode = "est"
        else:
            tokens = self.api.quote(SOL, mint, int(usd / sol * 1e9))
            if not tokens: return False
            mode = "jup"
        fees = self.cfg["priority_fee_usd"] + self.cfg["jito_tip_usd"]
        w.cash -= usd + fees
        w.open[mint] = dict(sym=sym, cost=usd, fees=fees, tokens=tokens, left=tokens, entry=price, peak=price, mode=mode,
                            creator=facts.get("creator"), dev_checked=facts.get("dev_checked") or int(now()), dev_t=now(),
                            got=0.0, half=False, t=now(), last_seen=now(), score=facts.get("score"), facts=facts)
        self.log("buy", wallet=wname, mint=mint, sym=sym, usd=round(usd, 2), price=price, **facts)
        if wname == "council": self.lab_mark(mint, "bought")
        return True

    def sell(self, wname, mint, part, why, pair=None):
        w = self.w[wname]; p = w.open[mint]; sol = self.sol_price() or 0
        amt = int(p["left"] * part) if part < 1 else p["left"]
        if p.get("mode") == "est" or self.api.jup_down():
            price = fnum((pair or {}).get("priceUsd"), 0) or 0
            gross = amt / 1e6 * price if p.get("mode") == "est" else amt / p["tokens"] * p["cost"] * (price / p["entry"] if p["entry"] else 0)
            usd = gross * (1 - EXCHANGE_FEE - est_impact(gross, pair)) if pair and price else 0.0
        else:
            out = self.api.quote(mint, SOL, amt)
            usd = (out / 1e9 * sol) if out else 0.0
        fees = self.cfg["priority_fee_usd"] + self.cfg["jito_tip_usd"]
        p["got"] += usd - fees; p["fees"] += fees; p["left"] -= amt; w.cash += usd - fees
        if p["left"] <= 0 or part >= 1:
            entry_fee = self.cfg["priority_fee_usd"] + self.cfg["jito_tip_usd"]
            pnl = p["got"] - p["cost"] - entry_fee   # got is already net of sell fees
            rec = dict(mint=mint, sym=p["sym"], cost=round(p["cost"], 2), back=round(p["got"], 2), pnl=round(pnl, 3),
                       why=why, score=p.get("score"), held_min=round((now() - p["t"]) / 60, 1), opened=iso(p["t"]), closed=iso())
            w.closed.append(rec); del w.open[mint]
            self.log("exit", wallet=wname, **rec)
        else:
            self.log("partial", wallet=wname, mint=mint, sym=p["sym"], usd=round(usd, 2), why=why)

    def manage(self):
        self.last_manage = now()
        mints = sorted({m for w in self.w.values() for m in w.open})
        if not mints: return
        pairs = self.api.pairs(mints)
        c = self.cfg
        for wname, w in self.w.items():
            for mint in list(w.open):
                p = w.open[mint]; pair = pairs.get(mint)
                if self.helius and p.get("creator") and now() - p.get("dev_t", 0) >= self.cfg["dev_watch_sec"]:
                    p["dev_t"] = now()
                    sold, last = self.helius.dev_sold_since(p["creator"], mint, since=p.get("dev_checked") or 0, max_tx=5)
                    p["dev_checked"] = max(p.get("dev_checked") or 0, last)
                    if sold:
                        self.sell(wname, mint, 1, "Dev wallet sold, got out", pair); continue
                price = fnum((pair or {}).get("priceUsd"))
                liq = fnum(((pair or {}).get("liquidity") or {}).get("usd"), 0) or 0
                tx1 = ((pair or {}).get("txns") or {}).get("h1") or {}
                active = (tx1.get("buys") or 0) + (tx1.get("sells") or 0) >= c["min_tx_h1"]
                if price and active and (liq > 500 or (pair or {}).get("dexId") == "pumpfun"):
                    p["last_seen"] = now()
                elif now() - p["last_seen"] > c["dead_minutes"] * 60:
                    self.sell(wname, mint, 1, "Coin died: no buyers", pair); continue
                else:
                    continue
                if not p["entry"]: p["entry"] = price
                p["mark"] = price
                x = price / p["entry"]; p["peak"] = max(p["peak"], price)
                if not p["half"] and x <= 1 - c["stop_pct"] / 100:
                    self.sell(wname, mint, 1, "Hard stop", pair)
                elif not p["half"] and x >= 1 + c["target_pct"] / 100:
                    p["half"] = True; self.sell(wname, mint, c["sell_part"], f"Sold {int(c['sell_part']*100)}% at target", pair)
                elif p["half"] and price <= p["peak"] * (1 - c["trail_pct"] / 100):
                    self.sell(wname, mint, 1, "Trailing stop", pair)

    def followups(self):
        due = [f for f in self.follow if now() - f["t"] >= self.cfg["followup_minutes"] * 60][:60]
        if not due: return
        pairs = self.api.pairs([f["mint"] for f in due])
        for f in due:
            price = fnum((pairs.get(f["mint"]) or {}).get("priceUsd"))
            r = f["reason"]; ch = self.stats["kills_checked"]; ch[r] = ch.get(r, 0) + 1
            if price and f["price"] and price / f["price"] >= self.cfg["pumped_x"]:
                pm = self.stats["kills_pumped"]; pm[r] = pm.get(r, 0) + 1
                self.log("missed", mint=f["mint"], reason=r, x=round(price / f["price"], 2))
        dset = {id(f) for f in due}
        self.follow = [f for f in self.follow if id(f) not in dset]

    def state(self):
        return dict(council=self.w["council"].dump(), control=self.w["control"].dump(),
                    seen=list(self.seen)[-20000:], follow=self.follow, retry=self.retry,
                    report_tries=dict(list(self.report_tries.items())[-5000:]), stats=self.stats, saved=iso())


# ------------------------------------------------------------------ report
def summarize(trades):
    n = len(trades)
    if not n: return dict(n=0)
    wins = [t["pnl"] for t in trades if t["pnl"] > 0]; losses = [t["pnl"] for t in trades if t["pnl"] <= 0]
    cost = sum(t["cost"] for t in trades)
    return dict(n=n, win_rate=100 * len(wins) / n, avg_win=sum(wins) / len(wins) if wins else 0,
                avg_loss=sum(losses) / len(losses) if losses else 0, exp=sum(t["pnl"] for t in trades) / n,
                ret_pct=100 * sum(t["pnl"] for t in trades) / cost if cost else 0,
                wl=(sum(wins) / -sum(losses)) if losses and sum(losses) < 0 else None)

def write_report(desk, net):
    c, k = desk.w["council"], desk.w["control"]
    sc, sk = summarize(c.closed), summarize(k.closed)
    L = [f"# Kill-First Desk · paper trading", "", f"Updated {iso()} UTC. Paper only: no wallet, no real trades.", ""]
    L += [f"Dev wallet watch (Helius): **{'on' if desk.helius else 'off'}**" + (f", {desk.helius.calls:,} calls this run" if desk.helius else ""), ""]
    if desk.api.jup_down():
        L += ["> Jupiter quotes are unavailable, so fills are **estimated** from pool depth plus the 1.25% exchange fee, "
              "and the honeypot sell test falls back to RugCheck's tax and transfer flags.", ""]
    L += ["## Wallets", "", "| | Council picks | Random control |", "|---|---|---|"]
    L += [f"| Value now | ${c.value():.2f} | ${k.value():.2f} |",
          f"| Started with | ${c.start:.2f} | ${k.start:.2f} |",
          f"| Open trades | {len(c.open)} | {len(k.open)} |",
          f"| Closed trades | {sc['n']} | {sk['n']} |"]
    if sc["n"] or sk["n"]:
        f = lambda s, key, fmt: (fmt.format(s[key]) if s.get("n") and s.get(key) is not None else "—")
        L += [f"| Win rate | {f(sc,'win_rate','{:.0f}%')} | {f(sk,'win_rate','{:.0f}%')} |",
              f"| Avg win | {f(sc,'avg_win','${:.2f}')} | {f(sk,'avg_win','${:.2f}')} |",
              f"| Avg loss | {f(sc,'avg_loss','${:.2f}')} | {f(sk,'avg_loss','${:.2f}')} |",
              f"| Expectancy per trade | {f(sc,'exp','${:+.3f}')} | {f(sk,'exp','${:+.3f}')} |",
              f"| Return per $ bet | {f(sc,'ret_pct','{:+.1f}%')} | {f(sk,'ret_pct','{:+.1f}%')} |"]
    L += ["", "## Does the council have an edge?", ""]
    if sc.get("n", 0) >= 30 and sk.get("n", 0) >= 30:
        gap = sc["ret_pct"] - sk["ret_pct"]
        L += [f"Council picks return {sc['ret_pct']:+.1f}% per dollar bet, random picks {sk['ret_pct']:+.1f}%. Gap: **{gap:+.1f} points**.",
              "A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing."]
    else:
        L += [f"Not enough trades yet. Need at least 30 closed trades in each wallet (now {sc.get('n',0)} and {sk.get('n',0)})."]
    st = desk.stats
    L += ["", f"Lab: {st.get('lab_done', 0):,} coins fully tracked for 4 hours, {len(desk.lab):,} still being followed. "
          "Run `python analyze.py` to see what predicted the winners (writes LEARN.md)."]
    L += ["", "## Funnel", "", f"Coins found: {st['found']:,} · young coins waiting for a second look: {len(desk.retry):,} · "
          f"RugCheck rechecks: {st.get('report_retries', 0):,} · coins matching the v3 pattern on sight: {st.get('v3_seen', 0):,}", "", "| Stopped because | Count | Checked 1h later | Pumped 2x+ |", "|---|---|---|---|"]
    for r, n in sorted(st["kills"].items(), key=lambda x: -x[1]):
        ch = st["kills_checked"].get(r, 0); pm = st["kills_pumped"].get(r, 0)
        L.append(f"| {r} | {n:,} | {ch:,} | {pm} ({100*pm/ch:.0f}%) |" if ch else f"| {r} | {n:,} | 0 | — |")
    L += ["", "## Recent council trades", "", "| Closed | Coin | Score | Exit | P&L |", "|---|---|---|---|---|"]
    for t in c.closed[-15:][::-1]:
        L.append(f"| {t['closed'][5:16]} | {t['sym']} | {t.get('score')} | {t['why']} | ${t['pnl']:+.2f} |")
    if net and net.errors:
        L += ["", "## Data source errors this run", ""] + [f"- {h}: {n}" for h, n in net.errors.items()]
    with open(REPORT, "w") as fh:
        fh.write("\n".join(L) + "\n")


# ------------------------------------------------------------------ mock API for offline tests
class MockAPI:
    def __init__(self, seed=1):
        self.r = random.Random(seed); self.coins = {}; self.n = 0; self.t0 = now()
    def _mk(self):
        self.n += 1; m = f"MOCK{self.n:05d}" + "x" * 30
        good = self.r.random() < 0.3
        self.coins[m] = dict(price=1e-5 * (1 + self.r.random()), drift=(0.004 if good else -0.004), alive=self.r.random() > 0.2,
                             vol=self.r.choice([5e3, 6e4, 2e5]), rug=self.r.random() < 0.3, hp=self.r.random() < 0.05)
        return m
    def new_profiles(self): return [("dexscreener", self._mk(), {"symbol": "DX"}) for _ in range(self.r.randint(0, 4))]
    def pump_newest(self): return [("pumpfun", self._mk(), {"symbol": "PF", "twitter": "x"}) for _ in range(self.r.randint(0, 4))]
    def pairs(self, mints):
        out = {}
        for m in mints:
            c = self.coins.get(m)
            if not c or not c["alive"]: continue
            c["price"] *= math.exp(c["drift"] + 0.08 * self.r.gauss(0, 1))
            if self.r.random() < 0.002: c["alive"] = False
            out[m] = {"baseToken": {"address": m, "symbol": m[:8]}, "dexId": "pumpfun", "priceUsd": str(c["price"]),
                      "liquidity": {"usd": 30000},
                      "txns": {"m5": {"buys": self.r.randint(0, 80), "sells": self.r.randint(0, 60)}, "h1": {"buys": self.r.randint(50, 900), "sells": self.r.randint(50, 600)}},
                      "pairCreatedAt": (self.t0 - 600) * 1000, "marketCap": self.r.choice([5e3, 2e4, 8e4, 2e6]), "priceChange": {"h1": self.r.uniform(-30, 150), "m5": self.r.uniform(-20, 40)}, "volume": {"h24": c["vol"], "h1": c["vol"] / 4, "m5": c["vol"] / 40},
                      "info": {"socials": [{"type": "twitter"}] * self.r.randint(0, 2)}}
        return out
    def rugcheck(self, m):
        c = self.coins[m]
        c["rc"] = c.get("rc", 0) + 1
        if c["rc"] == 1 and self.r.random() < 0.4: return None   # not indexed yet
        return {"mintAuthority": None, "freezeAuthority": "X" if c["hp"] else None, "creator": "DEV", "rugged": False,
                "topHolders": [{"owner": "DEV", "pct": 25 if c["rug"] else 3}] + [{"owner": f"H{i}", "pct": 2, "insider": False} for i in range(9)],
                "markets": [{"lp": {"lpLockedPct": 100}}], "risks": [], "totalHolders": self.r.randint(20, 2000)}
    def quote(self, i, o, amt):
        if o == USDC: return int(amt / 1e9 * 180 * 1e6)
        if i == SOL:
            c = self.coins.get(o)
            return int(amt / 1e9 * 180 / c["price"] * 1e6 * 0.98) if c else None
        c = self.coins.get(i)
        if not c or c["hp"] or not c["alive"]: return None
        return int(amt / 1e6 * c["price"] / 180 * 1e9 * 0.98)
    def sol_usd(self): return 180.0
    def jup_down(self): return False


def push_results():
    """Save the report and logs to the repo mid-run so REPORT.md stays fresh."""
    import subprocess
    sh = lambda *c: subprocess.run(c, cwd=os.path.dirname(os.path.abspath(__file__)), capture_output=True, text=True, timeout=120)
    try:
        sh("git", "add", "data", "REPORT.md")
        if sh("git", "diff", "--cached", "--quiet").returncode == 0: return
        sh("git", "commit", "-m", "Paper desk live update " + iso()[:16])
        for _ in range(3):
            if sh("git", "pull", "--rebase", "-X", "theirs").returncode == 0 and sh("git", "push").returncode == 0:
                print(f"{iso()} report saved to GitHub", flush=True); return
            sh("git", "rebase", "--abort"); time.sleep(5)
        print(f"{iso()} could not save report mid-run (will retry)", flush=True)
    except Exception as e:
        print(f"{iso()} push error {e!r}", flush=True)

# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=345)
    ap.add_argument("--poll", type=float, default=30, help="seconds between passes")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--push-every", type=float, default=10, help="minutes between saving results to GitHub mid-run")
    a = ap.parse_args()
    global DATA, REPORT
    if a.mock:
        CFG.update(followup_minutes=0.3, dead_minutes=0.1, dev_watch_sec=0)
        global LAB_SNAPS; LAB_SNAPS = (0.05, 0.1, 0.2)
        DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock-data")
        REPORT = os.path.join(DATA, "REPORT.md")
    os.makedirs(DATA, exist_ok=True)
    open(os.path.join(DATA, "api-debug.txt"), "w").close()
    sp = os.path.join(DATA, "state.json")
    state = json.load(open(sp)) if os.path.exists(sp) else None
    net = None if a.mock else Net()
    api = MockAPI() if a.mock else API(net)
    desk = Desk(api, CFG, state)
    hk = os.environ.get("HELIUS_API_KEY")
    if hk and not a.mock:
        desk.helius = Helius(net, hk); print(f"{iso()} Helius on: dev wallet checks and dev-sell exits", flush=True)
    else:
        print(f"{iso()} Helius off: no HELIUS_API_KEY", flush=True)
    end = now() + a.minutes * 60; last_save = 0; passes = 0; last_push = now()
    on_gh = os.environ.get("GITHUB_ACTIONS") == "true" and not a.mock
    print(f"{iso()} paper desk starting, council ${desk.w['council'].equity():.2f}, control ${desk.w['control'].equity():.2f}", flush=True)
    import signal
    stopping = []
    signal.signal(signal.SIGTERM, lambda *_: stopping.append(1))   # a cancelled run still saves its results
    while now() < end and not stopping:
        t0 = now()
        try:
            desk.scout(); desk.manage(); desk.followups(); desk.lab_update()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("pass error:", repr(e), flush=True)
        passes += 1
        if now() - last_save > (5 if a.mock else 300):
            json.dump(desk.state(), open(sp, "w")); write_report(desk, net); last_save = now()
            if on_gh and now() - last_push > a.push_every * 60:
                push_results(); last_push = now()
            print(f"{iso()} pass {passes} found {desk.stats['found']} kills {json.dumps(desk.stats['kills'])} errors {json.dumps(net.errors if net else {})}", flush=True)
            print(f"{iso()} pass {passes} found {desk.stats['found']} council ${desk.w['council'].equity():.2f} "
                  f"({len(desk.w['council'].open)} open) control ${desk.w['control'].equity():.2f}", flush=True)
        try: time.sleep(max(0, a.poll - (now() - t0)))
        except KeyboardInterrupt: break
    json.dump(desk.state(), open(sp, "w")); write_report(desk, net)
    json.dump(desk.lab, open(os.path.join(DATA, "lab-pending.json"), "w"), separators=(",", ":"))
    print(f"{iso()} done after {passes} passes, lab following {len(desk.lab)} coins", flush=True)

if __name__ == "__main__":
    main()
