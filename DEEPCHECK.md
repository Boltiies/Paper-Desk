# Independent check: RSI dip-buying

RSI(14): buy when it drops below 25, sell when it rises above 65. 18 Coinbase coins, daily candles from 2021-07-01, 0.95% per trade. Recomputed with vectorbt (a different engine from cex/backtest.py) as one portfolio: each coin gets an equal slice of the money and sits in cash when not holding.

RSI cross-check against TA-Lib: largest difference 33.9923 points, average 0.05923.

## $1,000 from 2021-07-01 to 2026-11-14

| | Ended with | Total | Per year | Worst drop | Sharpe |
|---|---|---|---|---|---|
| RSI dip-buying | $2,204 | +120% | +15.8% | -34% | 0.69 |
| Buy and hold basket | $616 | -38% | -8.5% | -82% | 0.19 |

Closed trades: 94 · win rate 62% · average trade +18.3% · median +6.3%.

## Year by year

| Year | RSI dip-buying | Buy and hold | Time in the market |
|---|---|---|---|
| 2021 | +64% | +52% | 4% |
| 2022 | +7% | -72% | 31% |
| 2023 | +8% | +84% | 16% |
| 2024 | +18% | +97% | 11% |
| 2025 | +3% | -39% | 6% |
| 2026 | -3% | -33% | 43% |

## Each coin

| Coin | RSI dip-buying | Buy and hold | Trades |
|---|---|---|---|
| AAVE | +33% | -56% | 2 |
| ADA | -55% | -88% | 4 |
| ATOM | -55% | -89% | 5 |
| AVAX | -33% | -88% | 4 |
| BCH | +29% | -58% | 4 |
| BTC | +13% | +93% | 9 |
| DOGE | +227% | -75% | 5 |
| DOT | -3% | -95% | 6 |
| ETH | +161% | -16% | 8 |
| LINK | +245% | -50% | 7 |
| LTC | +24% | -66% | 5 |
| NEAR | -4% | -23% | 5 |
| SHIB | +1249% | -58% | 5 |
| SOL | +50% | +118% | 8 |
| SUI | -36% | -33% | 5 |
| UNI | +280% | -71% | 6 |
| XLM | +66% | -49% | 4 |
| XRP | -22% | +12% | 2 |

Full QuantStats report (download and open in a browser): `reports/rsi-vs-hold.html`.
