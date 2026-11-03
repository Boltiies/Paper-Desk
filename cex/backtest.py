#!/usr/bin/env python3
"""
Backtests simple, well-known strategies on Coinbase daily candles and compares each
to just holding the coin. Honest by design:

  - Coinbase US fees: 0.90% taker (market orders) on every buy and every sell,
    plus 0.05% slippage. Change with --fee.
  - Signals use only data up to yesterday's close; trades fill at today's open.
  - Walk-forward: each strategy's settings are picked on the "train" years only,
    then judged on the "test" years it never saw.
  - Benchmarks: buy-and-hold of the same coin, and an equal-weight basket.

Run:  python cex/backtest.py                      (writes BACKTEST.md)
      python cex/backtest.py --split 2024-07-01   (move the train/test boundary)
"""
import argparse, glob, itertools, os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "data-cex", "coinbase")


# ------------------------------------------------------------------ data
def load(tf="1d"):
    out = {}
    for p in sorted(glob.glob(os.path.join(DATA, f"*-USD-{tf}.csv.gz"))):
        coin = os.path.basename(p).split("-")[0]
        df = pd.read_csv(p, parse_dates=["ts"]).set_index("ts").sort_index()
        df = df[~df.index.duplicated()]
        if len(df) > 400: out[coin] = df
    return out


# ------------------------------------------------------------------ strategies
# Each returns a 0/1 "want to be in the coin" series computed from data up to that bar's close.
def sma_cross(df, fast, slow):
    c = df["close"]; return (c.rolling(fast).mean() > c.rolling(slow).mean()).astype(float)

def above_sma(df, n):
    c = df["close"]; return (c > c.rolling(n).mean()).astype(float)

def donchian(df, entry, exit_):
    c, h, l = df["close"], df["high"], df["low"]
    up = h.rolling(entry).max().shift(1); dn = l.rolling(exit_).min().shift(1)
    pos = pd.Series(np.nan, index=df.index)
    pos[c > up] = 1.0; pos[c < dn] = 0.0
    return pos.ffill().fillna(0.0)

def rsi(c, n=14):
    d = c.diff(); up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean(); dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))

def rsi_revert(df, low, high):
    r = rsi(df["close"]); pos = pd.Series(np.nan, index=df.index)
    pos[r < low] = 1.0; pos[r > high] = 0.0
    return pos.ffill().fillna(0.0)

def bollinger_revert(df, n, k):
    c = df["close"]; m = c.rolling(n).mean(); s = c.rolling(n).std()
    pos = pd.Series(np.nan, index=df.index)
    pos[c < m - k * s] = 1.0; pos[c > m] = 0.0
    return pos.ffill().fillna(0.0)

def momentum(df, n):
    c = df["close"]; return (c / c.shift(n) - 1 > 0).astype(float)

STRATS = {
    "Moving-average cross": (sma_cross, [dict(fast=f, slow=s) for f, s in itertools.product([10, 20, 50], [50, 100, 200]) if f < s]),
    "Price above moving average": (above_sma, [dict(n=n) for n in (20, 50, 100, 200)]),
    "Breakout (Donchian)": (donchian, [dict(entry=e, exit_=x) for e, x in itertools.product([20, 55, 100], [10, 20, 50]) if x < e]),
    "Momentum": (momentum, [dict(n=n) for n in (14, 30, 60, 90, 180)]),
    "RSI dip-buying": (rsi_revert, [dict(low=lo, high=hi) for lo, hi in itertools.product([20, 25, 30, 35], [55, 65, 75])]),
    "Bollinger dip-buying": (bollinger_revert, [dict(n=n, k=k) for n, k in itertools.product([20, 50], [1.5, 2.0, 2.5])]),
}


# ------------------------------------------------------------------ simulation
def run(df, pos, fee):
    """Daily equity curve. pos[t] is decided at close t and held from open t+1."""
    o, c = df["open"], df["close"]
    held = pos.shift(1).fillna(0.0)                 # position during bar t
    prev = held.shift(1).fillna(0.0)
    # entering at open t: return open->close; staying: close(t-1)->close(t); leaving at open t: close(t-1)->open(t)
    r = np.where((held == 1) & (prev == 0), c / o - 1,
        np.where((held == 1) & (prev == 1), c / c.shift(1) - 1,
        np.where((held == 0) & (prev == 1), o / c.shift(1) - 1, 0.0)))
    trades = (held != prev).astype(float)
    r = pd.Series(r, index=df.index).fillna(0.0) - trades * fee
    return (1 + r).cumprod(), int(trades.sum())

def stats(eq, trades=None):
    if len(eq) < 30: return None
    r = eq.pct_change().dropna()
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    cagr = eq.iloc[-1] / eq.iloc[0]
    cagr = cagr ** (1 / yrs) - 1 if yrs > 0 and cagr > 0 else -1.0
    dd = (eq / eq.cummax() - 1).min()
    sharpe = r.mean() / r.std() * np.sqrt(365) if r.std() > 0 else 0.0
    return dict(total=eq.iloc[-1] / eq.iloc[0] - 1, cagr=cagr, maxdd=dd, sharpe=sharpe, trades=trades)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fee", type=float, default=0.0095, help="per trade: 0.90%% taker + 0.05%% slippage")
    ap.add_argument("--split", default="2024-07-01", help="train before, test from this date")
    ap.add_argument("--out", default=os.path.join(HERE, "BACKTEST.md"))
    a = ap.parse_args()
    data = load("1d")
    if not data: raise SystemExit("No data yet. Run the Coinbase data workflow first.")
    split = pd.Timestamp(a.split, tz="UTC")
    rows = []
    for name, (fn, grid) in STRATS.items():
        for coin, df in data.items():
            tr, te = df[df.index < split], df[df.index >= split]
            if len(tr) < 300 or len(te) < 60: continue
            best = None
            for params in grid:      # pick settings on the training years only
                eq, n = run(tr, fn(tr, **params), a.fee)
                s = stats(eq, n)
                if s and (best is None or s["sharpe"] > best[1]["sharpe"]): best = (params, s)
            params = best[0]
            # test: compute signals on the full history (indicators need warm-up), score only the test period
            full_pos = fn(df, **params)
            eq, n = run(te, full_pos.loc[te.index], a.fee)
            hold, _ = run(te, pd.Series(1.0, index=te.index), a.fee)
            st, sh = stats(eq, n), stats(hold)
            rows.append(dict(strategy=name, coin=coin, params=params, train_sharpe=best[1]["sharpe"],
                             **{f"t_{k}": v for k, v in st.items()}, **{f"h_{k}": v for k, v in sh.items() if k != "trades"}))
    R = pd.DataFrame(rows)
    # equal-weight basket benchmark over the test period
    closes = pd.DataFrame({c: d["close"] for c, d in data.items()})
    closes = closes[closes.index >= split].dropna(axis=1, thresh=int(0.9 * len(closes[closes.index >= split])))
    basket = (closes.pct_change().mean(axis=1).fillna(0) + 1).cumprod()
    bs = stats(basket)
    test_days = (closes.index[-1] - closes.index[0]).days

    pct = lambda x: f"{100*x:+.0f}%"
    L = ["# Coinbase strategy backtest", "",
         f"Daily candles for {len(data)} coins. Settings picked on data before **{a.split}**, then judged on "
         f"**{a.split} to {closes.index[-1]:%Y-%m-%d}** ({test_days} days), which they never saw. "
         f"Every buy and sell pays {100*a.fee:.2f}% (Coinbase US taker fee plus slippage).", "",
         f"Benchmark: an equal-weight basket of all coins returned **{pct(bs['total'])}** over the test period "
         f"(worst drop {pct(bs['maxdd'])}).", "",
         "## Each strategy, averaged over all coins (test period only)", "",
         "| Strategy | Avg return | Avg buy-and-hold | Beat holding on | Avg worst drop (vs holding) | Trades per coin |",
         "|---|---|---|---|---|---|"]
    for name, g in R.groupby("strategy", sort=False):
        beat = (g["t_total"] > g["h_total"]).mean()
        L.append(f"| {name} | {pct(g['t_total'].mean())} | {pct(g['h_total'].mean())} | {100*beat:.0f}% of coins | "
                 f"{pct(g['t_maxdd'].mean())} ({pct(g['h_maxdd'].mean())}) | {g['t_trades'].mean():.0f} |")
    L += ["", "## Every coin and strategy (test period)", "",
          "| Strategy | Coin | Settings (picked on training data) | Return | Holding | Worst drop | Holding drop | Sharpe | Trades |",
          "|---|---|---|---|---|---|---|---|---|"]
    for _, r in R.sort_values(["strategy", "coin"]).iterrows():
        ps = ", ".join(f"{k}={v}" for k, v in r["params"].items())
        L.append(f"| {r['strategy']} | {r['coin']} | {ps} | {pct(r['t_total'])} | {pct(r['h_total'])} | {pct(r['t_maxdd'])} | "
                 f"{pct(r['h_maxdd'])} | {r['t_sharpe']:.2f} | {int(r['t_trades'])} |")
    open(a.out, "w").write("\n".join(L) + "\n")
    R.to_csv(os.path.join(HERE, "data-cex", "backtest-results.csv"), index=False)
    print(f"wrote {a.out}: {len(R)} strategy/coin tests")
    return R, bs


if __name__ == "__main__":
    main()
