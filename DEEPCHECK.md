# Independent check: RSI dip-buying

RSI(14): buy when it drops below 25, sell when it rises above 65. 18 Coinbase coins, daily candles from 2021-07-01, 0.95% per trade. Recomputed with vectorbt (a different engine from cex/backtest.py) as one portfolio: each coin gets an equal slice of the money and sits in cash when not holding.

RSI cross-check against TA-Lib: largest difference 33.9923 points, average 0.05901.

## $1,000 from 2021-07-01 to 2026-11-21

| | Ended with | Total | Per year | Worst drop | Sharpe |
|---|---|---|---|---|---|
| RSI dip-buying | $2,082 | +108% | +14.6% | -34% | 0.64 |
| Buy and hold basket | $529 | -47% | -11.0% | -82% | 0.15 |

Closed trades: 100 · win rate 58% · average trade +16.4% · median +2.7%.

## Year by year

| Year | RSI dip-buying | Buy and hold | Time in the market |
|---|---|---|---|
| 2021 | +64% | +52% | 4% |
| 2022 | +7% | -72% | 31% |
| 2023 | +8% | +84% | 16% |
| 2024 | +18% | +97% | 11% |
| 2025 | +3% | -39% | 6% |
| 2026 | -8% | -42% | 44% |

## Each coin

| Coin | RSI dip-buying | Buy and hold | Trades |
|---|---|---|---|
| AAVE | +33% | -61% | 2 |
| ADA | -57% | -90% | 5 |
| ATOM | -55% | -90% | 5 |
| AVAX | -33% | -91% | 4 |
| BCH | +23% | -63% | 5 |
| BTC | -3% | +66% | 9 |
| DOGE | +207% | -79% | 6 |
| DOT | -10% | -96% | 7 |
| ETH | +119% | -30% | 8 |
| LINK | +245% | -57% | 7 |
| LTC | +23% | -72% | 6 |
| NEAR | -4% | -36% | 5 |
| SHIB | +1149% | -65% | 6 |
| SOL | +32% | +91% | 8 |
| SUI | -36% | -45% | 5 |
| UNI | +280% | -77% | 6 |
| XLM | +66% | -56% | 4 |
| XRP | -30% | +1% | 2 |

Full QuantStats report (download and open in a browser): `reports/rsi-vs-hold.html`.
