#!/usr/bin/env python3
"""
Independent check of RSI dip-buying with vectorbt, TA-Lib and QuantStats.

Recomputes the strategy as one portfolio across all coins (each coin gets an equal
slice of the money), using different code from cex/backtest.py, and compares it to an
equal-weight buy-and-hold basket. Writes DEEPCHECK.md and an interactive QuantStats
report at reports/rsi-vs-hold.html.

Run (needs vectorbt, quantstats, TA-Lib):  python cex/deep_check.py
"""
import glob, os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "cex"))
import backtest as bt

N, LOW, HIGH = 14, 25, 65          # the shared setting chosen in the robustness check
FEE = 0.0095                        # Coinbase US taker fee 0.90% + 0.05% slippage
START = "2021-07-01"


def main():
    import vectorbt as vbt
    import quantstats as qs
    try:
        import talib
    except Exception:
        talib = None

    data = bt.load("1d")
    opens = pd.DataFrame({c: d["open"] for c, d in data.items()})
    closes = pd.DataFrame({c: d["close"] for c, d in data.items()})
    s = pd.Timestamp(START, tz="UTC")
    lines = ["# Independent check: RSI dip-buying", "",
             f"RSI({N}): buy when it drops below {LOW}, sell when it rises above {HIGH}. "
             f"{len(data)} Coinbase coins, daily candles from {START}, {100*FEE:.2f}% per trade. "
             "Recomputed with vectorbt (a different engine from cex/backtest.py) as one portfolio: "
             "each coin gets an equal slice of the money and sits in cash when not holding.", ""]

    # RSI two ways: our own (Wilder smoothing) and TA-Lib's, to catch indicator bugs
    rsi = closes.apply(lambda c: bt.rsi(c.dropna(), N))
    if talib is not None:
        tl = closes.apply(lambda c: pd.Series(talib.RSI(c.dropna().values.astype(float), timeperiod=N), index=c.dropna().index))
        diff = (rsi - tl).abs().loc[s:].stack()
        lines += [f"RSI cross-check against TA-Lib: largest difference {diff.max():.4f} points, average {diff.mean():.5f}.", ""]
    else:
        lines += ["TA-Lib wasn't available on this run, so the RSI cross-check was skipped.", ""]

    # signals decided at the close, filled at the next day's open
    entries = (rsi < LOW).shift(1, fill_value=False).loc[s:]
    exits = (rsi > HIGH).shift(1, fill_value=False).loc[s:]
    px = opens.loc[s:]
    pf = vbt.Portfolio.from_signals(px, entries, exits, fees=FEE, init_cash=1000 / len(data), freq="1D")
    value = pf.value().sum(axis=1)
    # buy-and-hold basket: equal money in each coin on day one (or when it lists), same fee once
    hold = vbt.Portfolio.from_holding(px, fees=FEE, init_cash=1000 / len(data), freq="1D").value().sum(axis=1)

    def row(name, v):
        r = v.pct_change().dropna()
        dd = (v / v.cummax() - 1).min()
        yrs = (v.index[-1] - v.index[0]).days / 365.25
        cagr = (v.iloc[-1] / v.iloc[0]) ** (1 / yrs) - 1
        shp = r.mean() / r.std() * np.sqrt(365) if r.std() > 0 else 0
        return f"| {name} | ${v.iloc[-1]:,.0f} | {100*(v.iloc[-1]/v.iloc[0]-1):+.0f}% | {100*cagr:+.1f}% | {100*dd:.0f}% | {shp:.2f} |"

    lines += [f"## $1,000 from {START} to {value.index[-1]:%Y-%m-%d}", "",
              "| | Ended with | Total | Per year | Worst drop | Sharpe |", "|---|---|---|---|---|---|",
              row("RSI dip-buying", value), row("Buy and hold basket", hold), ""]
    trades = pf.trades.records_readable
    lines += [f"Closed trades: {len(trades):,} · win rate {100*(trades['PnL'] > 0).mean():.0f}% · "
              f"average trade {100*trades['Return'].mean():+.1f}% · median {100*trades['Return'].median():+.1f}%.", ""]

    lines += ["## Year by year", "", "| Year | RSI dip-buying | Buy and hold | Time in the market |", "|---|---|---|---|"]
    inmkt = (pf.assets() > 0).mean(axis=1)
    for y in sorted(set(value.index.year)):
        v, h = value[value.index.year == y], hold[hold.index.year == y]
        if len(v) < 20: continue
        lines.append(f"| {y} | {100*(v.iloc[-1]/v.iloc[0]-1):+.0f}% | {100*(h.iloc[-1]/h.iloc[0]-1):+.0f}% | {100*inmkt[inmkt.index.year == y].mean():.0f}% |")

    lines += ["", "## Each coin", "", "| Coin | RSI dip-buying | Buy and hold | Trades |", "|---|---|---|---|"]
    per = pf.total_return(); perh = vbt.Portfolio.from_holding(px, fees=FEE, freq="1D").total_return()
    ntr = pf.trades.count()
    for c in per.index:
        lines.append(f"| {c} | {100*per[c]:+.0f}% | {100*perh[c]:+.0f}% | {int(ntr[c])} |")

    os.makedirs(os.path.join(HERE, "reports"), exist_ok=True)
    rep = os.path.join(HERE, "reports", "rsi-vs-hold.html")
    try:
        qs.reports.html(value.pct_change().dropna().tz_localize(None), benchmark=hold.pct_change().dropna().tz_localize(None),
                        output=rep, title="RSI dip-buying vs buy-and-hold basket (Coinbase, paper)")
        lines += ["", "Full QuantStats report (download and open in a browser): `reports/rsi-vs-hold.html`."]
    except Exception as e:
        lines += ["", f"QuantStats report failed: {e!r}"]
    open(os.path.join(HERE, "DEEPCHECK.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
