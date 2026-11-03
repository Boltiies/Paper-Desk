# Independent check: RSI dip-buying

RSI(14): buy when it drops below 25, sell when it rises above 65. 18 Coinbase coins, daily candles from 2021-07-01, 0.95% per trade. Recomputed with vectorbt (a different engine from cex/backtest.py) as one portfolio: each coin gets an equal slice of the money and sits in cash when not holding.

RSI cross-check against TA-Lib: largest difference 33.9923 points, average 0.05962.

## $1,000 from 2021-07-01 to 2026-11-02

| | Ended with | Total | Per year | Worst drop | Sharpe |
|---|---|---|---|---|---|
| RSI dip-buying | $2,215 | +121% | +16.1% | -34% | 0.69 |
| Buy and hold basket | $729 | -27% | -5.6% | -82% | 0.24 |

Closed trades: 90 · win rate 64% · average trade +19.3% · median +10.0%.

## Year by year

| Year | RSI dip-buying | Buy and hold | Time in the market |
|---|---|---|---|
| 2021 | +64% | +52% | 4% |
| 2022 | +7% | -72% | 31% |
| 2023 | +8% | +84% | 16% |
| 2024 | +18% | +97% | 11% |
| 2025 | +3% | -39% | 6% |
| 2026 | -2% | -20% | 45% |

## Each coin

| Coin | RSI dip-buying | Buy and hold | Trades |
|---|---|---|---|
| AAVE | +33% | -47% | 2 |
| ADA | -55% | -86% | 4 |
| ATOM | -55% | -88% | 5 |
| AVAX | -33% | -87% | 4 |
| BCH | +29% | -47% | 4 |
| BTC | +14% | +121% | 8 |
| DOGE | +227% | -71% | 5 |
| DOT | -3% | -94% | 6 |
| ETH | +163% | -1% | 7 |
| LINK | +245% | -42% | 7 |
| LTC | +24% | -62% | 5 |
| NEAR | -4% | -4% | 5 |
| SHIB | +1249% | -53% | 5 |
| SOL | +62% | +163% | 7 |
| SUI | -36% | -24% | 5 |
| UNI | +280% | -63% | 6 |
| XLM | +66% | -41% | 4 |
| XRP | -18% | +39% | 1 |

Full QuantStats report (download and open in a browser): `reports/rsi-vs-hold.html`.
