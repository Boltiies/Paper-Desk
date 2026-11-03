#!/usr/bin/env python3
"""
Coinbase paper trader: RSI dip-buying on live daily prices, against a buy-and-hold basket.
Paper only: no account, no keys, no real orders.

Runs once a day right after the Coinbase data download:
  - Strategy wallet ($1,000): each coin has an equal slot (1/N of the wallet).
    Buy a coin when its daily RSI(14) closes below 25; sell when it closes above 65.
  - Basket wallet ($1,000): bought every coin in equal amounts on day one, never sells.
  - Fills use the latest hourly close, minus 0.95% per trade (Coinbase US taker fee
    plus slippage).
Writes PAPER-COINBASE.md and keeps its state in data-cex/paper/.

Run:  python cex/paper_rsi.py
"""
import json, os, sys
from datetime import datetime, timezone
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "cex"))
import backtest as bt

N, LOW, HIGH, FEE, START_CASH = 14, 25, 65, 0.0095, 1000.0
DIR = os.path.join(HERE, "data-cex", "paper")
STATE = os.path.join(DIR, "state.json")
REPORT = os.path.join(HERE, "PAPER-COINBASE.md")


def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


def log(kind, **kw):
    kw.update(t=now(), kind=kind)
    with open(os.path.join(DIR, "trades.jsonl"), "a") as fh: fh.write(json.dumps(kw) + "\n")
    print(kw, flush=True)


def main():
    os.makedirs(DIR, exist_ok=True)
    daily = bt.load("1d")
    hourly = bt.load("1h")
    coins = sorted(c for c in daily if c in hourly)
    price = {c: float(hourly[c]["close"].iloc[-1]) for c in coins}
    asof = max(hourly[c].index[-1] for c in coins)
    rsi = {c: float(bt.rsi(daily[c]["close"], N).iloc[-1]) for c in coins}

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
        if c in rsi and rsi[c] > HIGH:
            p = S["pos"].pop(c); got = p["qty"] * price[c] * (1 - FEE)
            S["cash"] += got
            log("sell", coin=c, rsi=round(rsi[c], 1), price=price[c], usd=round(got, 2), pnl=round(got - p["cost"], 2),
                ret=round(got / p["cost"] - 1, 4), held_days=round((pd.Timestamp.now(tz="UTC") - pd.Timestamp(p["t"])).days))
    equity = S["cash"] + sum(p["qty"] * price[c] for c, p in S["pos"].items())
    size = equity / len(st["coins"])
    for c in st["coins"]:
        if c in S["pos"] or c not in rsi or rsi[c] >= LOW: continue
        usd = min(size, S["cash"])
        if usd < 1: continue
        S["cash"] -= usd
        S["pos"][c] = dict(qty=usd * (1 - FEE) / price[c], cost=usd, t=datetime.now(timezone.utc).isoformat(), entry=price[c])
        log("buy", coin=c, rsi=round(rsi[c], 1), price=price[c], usd=round(usd, 2))

    sv = S["cash"] + sum(p["qty"] * price[c] for c, p in S["pos"].items() if c in price)
    bv = sum(q * price[c] for c, q in st["basket"]["pos"].items() if c in price)
    st["history"].append(dict(t=now(), strat=round(sv, 2), basket=round(bv, 2)))
    json.dump(st, open(STATE, "w"), indent=1)

    trades = [json.loads(l) for l in open(os.path.join(DIR, "trades.jsonl"))] if os.path.exists(os.path.join(DIR, "trades.jsonl")) else []
    sells = [t for t in trades if t["kind"] == "sell"]
    L = ["# Coinbase paper trader · RSI dip-buying", "",
         f"Updated {now()} UTC, prices as of {asof:%Y-%m-%d %H:%M} UTC. Paper only: no account, no real orders.", "",
         f"Rule: buy a coin when its daily RSI({N}) closes below {LOW}, sell when it closes above {HIGH}. "
         f"Each coin gets an equal slot. Every trade pays {100*FEE:.2f}%. Started {st['started']} UTC.", "",
         "| | RSI dip-buying | Buy-and-hold basket |", "|---|---|---|",
         f"| Value now | ${sv:,.2f} | ${bv:,.2f} |",
         f"| Change | {100*(sv/START_CASH-1):+.1f}% | {100*(bv/START_CASH-1):+.1f}% |",
         f"| Cash | ${S['cash']:,.2f} | $0.00 |",
         f"| Coins held | {len(S['pos'])} of {len(st['coins'])} | {len(st['coins'])} |",
         f"| Closed trades | {len(sells)} | — |"]
    if sells:
        L.append(f"| Win rate | {100*sum(t['pnl'] > 0 for t in sells)/len(sells):.0f}% | — |")
    L += ["", "## Holdings", "", "| Coin | Bought at | Now | Change | RSI now |", "|---|---|---|---|---|"]
    for c, p in sorted(S["pos"].items()):
        L.append(f"| {c} | ${p['entry']:,.6g} | ${price[c]:,.6g} | {100*(price[c]/p['entry']-1):+.1f}% | {rsi[c]:.0f} |")
    if not S["pos"]: L.append("| — | No coins held. Waiting for a dip below RSI 25. | | | |")
    L += ["", "## Watch list (RSI now)", "", "Closest to a buy signal first.", "", "| Coin | RSI | Price |", "|---|---|---|"]
    for c in sorted(coins, key=lambda c: rsi[c]):
        L.append(f"| {c} | {rsi[c]:.0f}{' · buy zone' if rsi[c] < LOW else ' · sell zone' if rsi[c] > HIGH else ''} | ${price[c]:,.6g} |")
    L += ["", "## Recent trades", "", "| When | Action | Coin | RSI | Price | Result |", "|---|---|---|---|---|---|"]
    for t in [t for t in trades if t["kind"] in ("buy", "sell")][-20:][::-1]:
        res = f"{'+' if t['pnl'] > 0 else ''}${t['pnl']:.2f} ({100*t['ret']:+.0f}%)" if t["kind"] == "sell" else f"${t['usd']:.2f}"
        L.append(f"| {t['t']} | {t['kind']} | {t['coin']} | {t['rsi']} | ${t['price']:,.6g} | {res} |")
    open(REPORT, "w").write("\n".join(L) + "\n")
    print(f"strategy ${sv:,.2f} vs basket ${bv:,.2f}")


if __name__ == "__main__":
    main()
