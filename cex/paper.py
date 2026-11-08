#!/usr/bin/env python3
"""
Coinbase paper trader: a daily strategy on live prices, against a buy-and-hold basket.
Paper only: no account, no keys, no real orders.

Strategies (--strategy):
  rsi  RSI dip-buying: buy when daily RSI(14) closes below 25, sell when it closes above 65.
       Trades rarely: a few times a year per coin.
  ma   Moving-average cross: hold a coin while its 10-day average is above its 50-day
       average. Trades about 10 times a year per coin. Weaker in backtests (median
       coin-year slightly negative) but gives feedback much faster.

Runs once a day right after the Coinbase data download:
  - Strategy wallet ($1,000): each coin has an equal slot (1/N of the wallet).
  - Basket wallet ($1,000): bought every coin in equal amounts on day one, never sells.
  - Fills use the latest hourly close, minus 0.95% per trade (Coinbase US taker fee
    plus slippage).
rsi writes PAPER-COINBASE.md (state in data-cex/paper/);
ma writes PAPER-COINBASE-MA.md (state in data-cex/paper-ma/). Each has its own basket.

Run:  python cex/paper.py --strategy rsi
      python cex/paper.py --strategy ma
"""
import json, os, sys
from datetime import datetime, timezone
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "cex"))
import backtest as bt

N, LOW, HIGH, FEE, START_CASH = 14, 25, 65, 0.0095, 1000.0
FAST, SLOW = 10, 50
STRATS = {
    "rsi": dict(dir="paper", report="PAPER-COINBASE.md", title="RSI dip-buying",
                rule=f"buy a coin when its daily RSI({N}) closes below {LOW}, sell when it closes above {HIGH}."),
    "ma": dict(dir="paper-ma", report="PAPER-COINBASE-MA.md", title="Moving-average cross",
               rule=f"hold a coin while its {FAST}-day moving average is above its {SLOW}-day moving average; sell when it drops below."),
}
DIR = STATE = REPORT = None


def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


def log(kind, **kw):
    kw.update(t=now(), kind=kind)
    with open(os.path.join(DIR, "trades.jsonl"), "a") as fh: fh.write(json.dumps(kw) + "\n")
    print(kw, flush=True)


def main():
    import argparse
    global DIR, STATE, REPORT
    ap = argparse.ArgumentParser(); ap.add_argument("--strategy", choices=list(STRATS), default="rsi")
    a = ap.parse_args(); cfg = STRATS[a.strategy]
    DIR = os.path.join(HERE, "data-cex", cfg["dir"]); STATE = os.path.join(DIR, "state.json"); REPORT = os.path.join(HERE, cfg["report"])
    os.makedirs(DIR, exist_ok=True)
    daily = bt.load("1d")
    hourly = bt.load("1h")
    coins = sorted(c for c in daily if c in hourly)
    price = {c: float(hourly[c]["close"].iloc[-1]) for c in coins}
    asof = max(hourly[c].index[-1] for c in coins)
    rsi = {c: float(bt.rsi(daily[c]["close"], N).iloc[-1]) for c in coins}
    trend = {}
    for c in coins:
        cl = daily[c]["close"]; f, s = cl.rolling(FAST).mean().iloc[-1], cl.rolling(SLOW).mean().iloc[-1]
        trend[c] = (f / s - 1) * 100 if s == s and s > 0 else float("nan")      # % the fast average is above the slow one
    if a.strategy == "rsi":
        want_out = lambda c: rsi[c] > HIGH
        want_in = lambda c: rsi[c] < LOW
    else:
        want_out = lambda c: not trend[c] > 0
        want_in = lambda c: trend[c] > 0

    st = json.load(open(STATE)) if os.path.exists(STATE) else None
    if st is None:
        st = dict(started=now(), coins=coins, strat=dict(cash=START_CASH, pos={}),
                  basket=dict(pos={c: (START_CASH / len(coins)) * (1 - FEE) / price[c] for c in coins}),
                  history=[])
        log("start", note=f"basket bought {len(coins)} coins equally", prices=price)
    S = st["strat"]
    slot = START_CASH / len(st["coins"])

    # sells first, then buys, all at the current price
    for c in list(S["pos"]):
        if c in rsi and want_out(c):
            p = S["pos"].pop(c); got = p["qty"] * price[c] * (1 - FEE)
            S["cash"] += got
            log("sell", coin=c, rsi=round(rsi[c], 1), trend=round(trend[c], 2), price=price[c], usd=round(got, 2), pnl=round(got - p["cost"], 2),
                ret=round(got / p["cost"] - 1, 4), held_days=round((pd.Timestamp.now(tz="UTC") - pd.Timestamp(p["t"])).days))
    equity = S["cash"] + sum(p["qty"] * price[c] for c, p in S["pos"].items())
    size = equity / len(st["coins"])
    for c in st["coins"]:
        if c in S["pos"] or c not in rsi or not want_in(c): continue
        usd = min(size, S["cash"])
        if usd < 1: continue
        S["cash"] -= usd
        S["pos"][c] = dict(qty=usd * (1 - FEE) / price[c], cost=usd, t=datetime.now(timezone.utc).isoformat(), entry=price[c])
        log("buy", coin=c, rsi=round(rsi[c], 1), trend=round(trend[c], 2), price=price[c], usd=round(usd, 2))

    sv = S["cash"] + sum(p["qty"] * price[c] for c, p in S["pos"].items() if c in price)
    bv = sum(q * price[c] for c, q in st["basket"]["pos"].items() if c in price)
    st["history"].append(dict(t=now(), strat=round(sv, 2), basket=round(bv, 2)))
    json.dump(st, open(STATE, "w"), indent=1)

    trades = [json.loads(l) for l in open(os.path.join(DIR, "trades.jsonl"))] if os.path.exists(os.path.join(DIR, "trades.jsonl")) else []
    sells = [t for t in trades if t["kind"] == "sell"]
    L = [f"# Coinbase paper trader · {cfg['title']}", "",
         f"Updated {now()} UTC, prices as of {asof:%Y-%m-%d %H:%M} UTC. Paper only: no account, no real orders.", "",
         f"Rule: {cfg['rule']} "
         f"Each coin gets an equal slot. Every trade pays {100*FEE:.2f}%. Started {st['started']} UTC.", "",
         f"| | {cfg['title']} | Buy-and-hold basket |", "|---|---|---|",
         f"| Value now | ${sv:,.2f} | ${bv:,.2f} |",
         f"| Change | {100*(sv/START_CASH-1):+.1f}% | {100*(bv/START_CASH-1):+.1f}% |",
         f"| Cash | ${S['cash']:,.2f} | $0.00 |",
         f"| Coins held | {len(S['pos'])} of {len(st['coins'])} | {len(st['coins'])} |",
         f"| Closed trades | {len(sells)} | — |"]
    if sells:
        L.append(f"| Win rate | {100*sum(t['pnl'] > 0 for t in sells)/len(sells):.0f}% | — |")
    ind = (lambda c: f"RSI {rsi[c]:.0f}") if a.strategy == "rsi" else (lambda c: f"{trend[c]:+.1f}%")
    ind_name = "RSI now" if a.strategy == "rsi" else f"{FAST}d vs {SLOW}d average"
    L += ["", "## Holdings", "", f"| Coin | Bought at | Now | Change | {ind_name} |", "|---|---|---|---|---|"]
    for c, p in sorted(S["pos"].items()):
        L.append(f"| {c} | ${p['entry']:,.6g} | ${price[c]:,.6g} | {100*(price[c]/p['entry']-1):+.1f}% | {ind(c)} |")
    if not S["pos"]: L.append("| — | No coins held. Waiting for a buy signal. | | | |")
    if a.strategy == "rsi":
        L += ["", "## Watch list (RSI now)", "", "Closest to a buy signal first.", "", "| Coin | RSI | Price |", "|---|---|---|"]
        for c in sorted(coins, key=lambda c: rsi[c]):
            L.append(f"| {c} | {rsi[c]:.0f}{' · buy zone' if rsi[c] < LOW else ' · sell zone' if rsi[c] > HIGH else ''} | ${price[c]:,.6g} |")
    else:
        L += ["", f"## Watch list ({FAST}-day vs {SLOW}-day average)", "", "Positive means uptrend (held), negative means downtrend (not held). Closest to flipping first.", "",
              "| Coin | Gap | Price |", "|---|---|---|"]
        for c in sorted(coins, key=lambda c: abs(trend[c]) if trend[c] == trend[c] else 1e9):
            L.append(f"| {c} | {trend[c]:+.1f}% | ${price[c]:,.6g} |")
    L += ["", "## Recent trades", "", f"| When | Action | Coin | {'RSI' if a.strategy == 'rsi' else 'Gap'} | Price | Result |", "|---|---|---|---|---|---|"]
    for t in [t for t in trades if t["kind"] in ("buy", "sell")][-20:][::-1]:
        res = f"{'+' if t['pnl'] > 0 else ''}${t['pnl']:.2f} ({100*t['ret']:+.0f}%)" if t["kind"] == "sell" else f"${t['usd']:.2f}"
        iv = t.get("rsi") if a.strategy == "rsi" else f"{t.get('trend', 0):+.1f}%"
        L.append(f"| {t['t']} | {t['kind']} | {t['coin']} | {iv} | ${t['price']:,.6g} | {res} |")
    open(REPORT, "w").write("\n".join(L) + "\n")
    print(f"strategy ${sv:,.2f} vs basket ${bv:,.2f}")


if __name__ == "__main__":
    main()
