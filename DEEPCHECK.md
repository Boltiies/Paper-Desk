# Independent check: RSI dip-buying

RSI(14): buy when it drops below 25, sell when it rises above 65. 18 Coinbase coins, daily candles from 2021-07-01, 0.95% per trade. Recomputed with vectorbt (a different engine from cex/backtest.py) as one portfolio: each coin gets an equal slice of the money and sits in cash when not holding.

RSI cross-check against TA-Lib: largest difference 33.9923 points, average 0.05946.

## $1,000 from 2021-07-01 to 2026-11-07

| | Ended with | Total | Per year | Worst drop | Sharpe |
|---|---|---|---|---|---|
| RSI dip-buying | $2,215 | +121% | +16.0% | -34% | 0.69 |
| Buy and hold basket | $692 | -30% | -6.5% | -82% | 0.23 |

Closed trades: 90 · win rate 64% · average trade +19.3% · median +10.0%.

## Year by year

| Year | RSI dip-buying | Buy and hold | Time in the market |
|---|---|---|---|
| 2021 | +64% | +52% | 4% |
| 2022 | +7% | -72% | 31% |
| 2023 | +8% | +84% | 16% |
| 2024 | +18% | +97% | 11% |
| 2025 | +3% | -39% | 6% |
| 2026 | -2% | -24% | 44% |

## Each coin

| Coin | RSI dip-buying | Buy and hold | Trades |
|---|---|---|---|
| AAVE | +33% | -48% | 2 |
| ADA | -55% | -87% | 4 |
| ATOM | -55% | -89% | 5 |
| AVAX | -33% | -88% | 4 |
| BCH | +29% | -50% | 4 |
| BTC | +14% | +114% | 8 |
| DOGE | +227% | -72% | 5 |
| DOT | -3% | -94% | 6 |
| ETH | +163% | -3% | 7 |
| LINK | +245% | -45% | 7 |
| LTC | +24% | -64% | 5 |
| NEAR | -4% | -17% | 5 |
| SHIB | +1249% | -55% | 5 |
| SOL | +62% | +151% | 7 |
| SUI | -36% | -26% | 5 |
| UNI | +280% | -65% | 6 |
| XLM | +66% | -47% | 4 |
| XRP | -18% | +31% | 1 |

Full QuantStats report (download and open in a browser): `reports/rsi-vs-hold.html`.
