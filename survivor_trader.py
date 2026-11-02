#!/usr/bin/env python3
"""
Survivor desk: paper trades coins that already survived their launch.

Every version of the new-coin desk lost money because it was late: snipers and insiders
are in within seconds and sell to everyone after them. This desk stays out of that race.
It only looks at coins that graduated from the pump.fun curve and are still actively
trading at least a day after launch, and it trades on a slower clock.

Universe (all must hold):  graduated (not on the bonding curve), 1 to 30 days old,
  liquidity $25k+, 24h volume $50k+, market cap $100k-$50M, 30+ trades in the last hour,
  and the usual security checks.
Council signal (fixed before the test, not tuned):  survived a crash and is bouncing.
  Down 20-60% over 24 hours, up over the last hour, buys 55%+ of the last 5 minutes.
Random control:  buys a random sample of the same universe, ignoring the signal.
Exits:  -25% stop, sell half at +50%, 25% trailing stop on the rest, sell after 24 hours.

Same paper rules as the main desk: no wallet, no real trades, Jupiter quotes for fills.

Run:   python survivor_trader.py --minutes 340
Mock:  python survivor_trader.py --mock --minutes 1 --poll 0.1
"""
import argparse, json, os, random, subprocess, time
import paper_trader as pt

HERE = os.path.dirname(os.path.abspath(__file__))
pt.DATA = os.path.join(HERE, "data-survivors")
pt.REPORT = os.path.join(HERE, "SURVIVORS.md")
pt.LAB_SNAPS = (60, 240, 720, 1440)   # survivors move slower: follow each for a day

pt.CFG.update(
    stop_pct=25.0, target_pct=50.0, sell_part=0.5, trail_pct=25.0,
    max_hold_h=24, max_open=5, bet_pct=2.0, daily_loss_pct=40.0,
    max_h1_change=1e9, max_roundtrip_loss=8.0,
    min_age_h=24, max_age_d=30, uni_liq=25_000, uni_vol=50_000, uni_mcap=(1e5, 5e7), uni_tx_h1=30,
    control_prob=0.15, recheck_h=6, dev_watch_sec=10**9,
)
CFG = pt.CFG
G = lambda f, k, d: f.get(k) if f.get(k) is not None else d


def in_universe(pair, f):
    if not pair or (pair.get("dexId") or "") in ("pumpfun", "pump", "moonshot", "launchlab", "meteora-dbc", "meteoradbc"):
        return False, "Still on the launch curve"
    age_h = (G(f, "age_min", 0) or 0) / 60
    if age_h < CFG["min_age_h"]: return False, "Younger than a day"
    if age_h > CFG["max_age_d"] * 24: return False, "Older than 30 days"
    if f["liq"] < CFG["uni_liq"]: return False, "Liquidity too low"
    if f["vol_h24"] < CFG["uni_vol"]: return False, "Volume too low"
    lo, hi = CFG["uni_mcap"]
    if not lo <= f["mcap"] < hi: return False, "Market cap outside $100k-$50M"
    if f["tx_h1"] < CFG["uni_tx_h1"]: return False, "Too little trading"
    return True, ""


def survivor_signal(f):
    """Survived a crash and bouncing. Fixed before the test so the result can't be tuned to luck."""
    return (-60 <= G(f, "ch_h24", 0) <= -20 and G(f, "ch_h1", -1) > 0 and G(f, "ratio_m5", 0) >= 0.55)


def gecko_pools(net):
    """Older, busy Solana pools from GeckoTerminal. Optional: the desk still works if this fails."""
    out = []
    hdr = {"Accept": "application/json;version=20230302"}
    for path in ("trending_pools?page=1", "trending_pools?page=2", "pools?page=1&sort=h24_volume_usd_desc",
                 "pools?page=2&sort=h24_volume_usd_desc", "pools?page=3&sort=h24_volume_usd_desc"):
        d = net.get("https://api.geckoterminal.com/api/v2/networks/solana/" + path, gap=2.2, headers=hdr) or {}
        for p in d.get("data") or []:
            tid = (((p.get("relationships") or {}).get("base_token") or {}).get("data") or {}).get("id", "")
            if tid.startswith("solana_"): out.append(tid[7:])
    return out


class SurvivorDesk(pt.Desk):
    def __init__(self, api, net, state=None):
        super().__init__(api, CFG, state)
        st = state or {}
        self.net = net
        self.watch = st.get("watch", {})          # mint -> {"src", "added"}
        self.checked = st.get("checked", {})      # mint -> last time judged for the control lottery
        self.rc = st.get("rc", {})                # mint -> (time, report) cache
        self.last_watch = 0

    def state(self):
        d = super().state()
        d.update(watch=self.watch, checked=dict(list(self.checked.items())[-5000:]),
                 rc={k: v for k, v in list(self.rc.items())[-400:]})
        return d

    def refresh_watch(self):
        """Survivors from the main desk's lab (coins still alive at 4 hours) plus GeckoTerminal's busy pools."""
        if pt.now() - self.last_watch < 600: return
        self.last_watch = pt.now()
        lab = os.path.join(HERE, "data", "lab.jsonl")
        if os.path.exists(lab):
            for line in open(lab):
                try: r = json.loads(line)
                except ValueError: continue
                s = r.get("snaps") or {}
                if s and s[max(s, key=float)] > 0 and pt.now() - r["t0"] < CFG["max_age_d"] * 86400:
                    self.watch.setdefault(r["mint"], {"src": "lab", "added": pt.now()})
        if self.net:
            for m in gecko_pools(self.net):
                self.watch.setdefault(m, {"src": "gecko", "added": pt.now()})
        self.stats["watching"] = len(self.watch)

    def scout(self):
        self.refresh_watch()
        mints = list(self.watch)
        if not mints: return
        pairs = self.api.pairs(mints)
        for mint in mints:
            if pt.now() - self.last_manage > 20: self.manage()
            pair = pairs.get(mint)
            if not pair:
                self.watch.pop(mint, None); continue      # gone from the market
            self.decide(mint, pair)

    def report_for(self, mint):
        hit = self.rc.get(mint)
        if hit and pt.now() - hit[0] < 86400: return hit[1]
        rep = self.api.rugcheck(mint)
        if rep:
            keep = {k: rep.get(k) for k in ("mintAuthority", "freezeAuthority", "creator", "rugged", "topHolders",
                                             "knownAccounts", "risks", "markets", "totalHolders")}
            keep["markets"] = [{"lp": (m.get("lp") or {})} for m in (keep["markets"] or [])][:3]
            self.rc[mint] = (pt.now(), keep)
            return keep
        return None

    def decide(self, mint, pair):
        f = pt.features(pair, None)
        ok, why = in_universe(pair, f)
        sym = (pair.get("baseToken") or {}).get("symbol") or mint[:6]
        if not ok:
            return
        self.stats["in_universe"] = self.stats.get("in_universe", 0) + (0 if mint in self.checked else 1)
        sig = survivor_signal(f)
        lottery_due = pt.now() - self.checked.get(mint, 0) > CFG["recheck_h"] * 3600
        if lottery_due: self.checked[mint] = pt.now()
        ctrl = lottery_due and random.random() < CFG["control_prob"]
        if lottery_due: self.lab_add(mint, sym, pair, None, None, {})
        if not (sig or ctrl): return
        if all(mint in w.open or any(t["mint"] == mint for t in w.closed[-500:]) for w in self.w.values()): return
        rep = self.report_for(mint)
        if not rep: return
        ok, why, facts = pt.security(rep, pair, CFG, min_vol=0)
        price = pt.fnum(pair.get("priceUsd"))
        if not ok:
            self.lab_mark(mint, why); return self.kill(mint, sym, why, price, **facts)
        sol = self.sol_price()
        if not sol: return
        bet = max(1.0, self.w["council"].equity() * CFG["bet_pct"] / 100)
        got = self.api.quote(pt.SOL, mint, int(bet / sol * 1e9))
        back = self.api.quote(mint, pt.SOL, got) if got else None
        if not got or not back:
            return self.kill(mint, sym, "Sell test failed (honeypot or no route)", price, **facts)
        rt = 100 * (1 - back / int(bet / sol * 1e9))
        facts.update(roundtrip_loss=round(rt, 1), fills="jupiter", signal=sig, **f)
        if rt > CFG["max_roundtrip_loss"]:
            return self.kill(mint, sym, "Sell test: fees or impact too high", price, **facts)
        if sig:
            self.lab_mark(mint, "signal")
            self.buy("council", mint, sym, pair, facts, sol)
        if ctrl:
            self.buy("control", mint, sym, pair, facts, sol)

    def manage(self):
        # time stop first, then the normal stop / target / trail / dead-coin rules
        for wname, w in self.w.items():
            for mint in list(w.open):
                if pt.now() - w.open[mint]["t"] > CFG["max_hold_h"] * 3600:
                    pair = self.api.pairs([mint]).get(mint)
                    self.sell(wname, mint, 1, "Held 24 hours", pair)
        super().manage()


def push_results():
    sh = lambda *c: subprocess.run(c, cwd=HERE, capture_output=True, text=True, timeout=120)
    try:
        sh("git", "add", "data-survivors", "SURVIVORS.md")
        if sh("git", "diff", "--cached", "--quiet").returncode == 0: return
        sh("git", "commit", "-m", "Survivor desk live update " + pt.iso()[:16])
        for _ in range(3):
            if sh("git", "pull", "--rebase", "-X", "theirs").returncode == 0 and sh("git", "push").returncode == 0:
                print(f"{pt.iso()} survivor report saved to GitHub", flush=True); return
            sh("git", "rebase", "--abort"); time.sleep(5)
    except Exception as e:
        print(f"{pt.iso()} push error {e!r}", flush=True)


def write_report(desk, net):
    pt.write_report(desk, net)
    txt = open(pt.REPORT).read()
    txt = txt.replace("# Kill-First Desk · paper trading", "# Survivor desk · paper trading", 1)
    txt = txt.replace("Council picks", "Survivor signal").replace("## Does the council have an edge?", "## Does the survivor signal have an edge?")
    head = (f"\nWatching {len(desk.watch):,} survivor coins · {desk.stats.get('in_universe', 0):,} have passed the universe checks. "
            "Signal: down 20-60% over 24h, up over the last hour, buys 55%+ of the last 5 minutes.\n")
    txt = txt.replace("\n## Wallets", head + "\n## Wallets", 1)
    open(pt.REPORT, "w").write(txt)


class MockSurvivorAPI(pt.MockAPI):
    def __init__(self):
        super().__init__(seed=7)
        self.pool = [self._mk() for _ in range(80)]
    def pairs(self, mints):
        out = super().pairs(mints)
        for m, p in out.items():
            p.update(dexId="pumpswap", pairCreatedAt=(pt.now() - 3 * 86400) * 1000, marketCap=self.r.choice([5e4, 4e5, 2e6]),
                     liquidity={"usd": self.r.choice([1e4, 6e4])})
            p["priceChange"] = {"h24": self.r.uniform(-70, 40), "h1": self.r.uniform(-10, 15), "m5": self.r.uniform(-5, 5)}
            p["volume"] = {"h24": 3e5, "h1": 2e4, "m5": 2e3}
        return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=340)
    ap.add_argument("--poll", type=float, default=120)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--push-every", type=float, default=10)
    a = ap.parse_args()
    if a.mock:
        pt.DATA = os.path.join(HERE, "mock-survivors"); pt.REPORT = os.path.join(pt.DATA, "SURVIVORS.md")
        pt.LAB_SNAPS = (0.05, 0.1); CFG.update(dead_minutes=0.1, max_hold_h=0.01)
    os.makedirs(pt.DATA, exist_ok=True)
    open(os.path.join(pt.DATA, "api-debug.txt"), "w").close()
    sp = os.path.join(pt.DATA, "state.json")
    state = json.load(open(sp)) if os.path.exists(sp) else None
    net = None if a.mock else pt.Net()
    api = MockSurvivorAPI() if a.mock else pt.API(net)
    desk = SurvivorDesk(api, net, state)
    if a.mock:
        for m in api.pool: desk.watch[m] = {"src": "mock", "added": pt.now()}
        desk.last_watch = pt.now()
    hk = os.environ.get("HELIUS_API_KEY")
    if hk and not a.mock: desk.helius = pt.Helius(net, hk)
    on_gh = os.environ.get("GITHUB_ACTIONS") == "true" and not a.mock
    import signal
    stopping = []
    signal.signal(signal.SIGTERM, lambda *_: stopping.append(1))
    end = pt.now() + a.minutes * 60; last_save = 0; last_push = pt.now(); passes = 0
    print(f"{pt.iso()} survivor desk starting, signal ${desk.w['council'].equity():.2f}, control ${desk.w['control'].equity():.2f}", flush=True)
    while pt.now() < end and not stopping:
        t0 = pt.now()
        try:
            desk.scout(); desk.manage(); desk.followups(); desk.lab_update()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("pass error:", repr(e), flush=True)
        passes += 1
        if pt.now() - last_save > (3 if a.mock else 300):
            json.dump(desk.state(), open(sp, "w")); write_report(desk, net); last_save = pt.now()
            print(f"{pt.iso()} pass {passes} watching {len(desk.watch)} universe {desk.stats.get('in_universe', 0)} "
                  f"signal ${desk.w['council'].value():.2f} ({len(desk.w['council'].open)} open) control ${desk.w['control'].value():.2f}", flush=True)
            if on_gh and pt.now() - last_push > a.push_every * 60:
                push_results(); last_push = pt.now()
        try: time.sleep(max(0, a.poll - (pt.now() - t0)))
        except KeyboardInterrupt: break
    json.dump(desk.state(), open(sp, "w")); write_report(desk, net)
    json.dump(desk.lab, open(os.path.join(pt.DATA, "lab-pending.json"), "w"), separators=(",", ":"))
    print(f"{pt.iso()} done after {passes} passes", flush=True)


if __name__ == "__main__":
    main()
