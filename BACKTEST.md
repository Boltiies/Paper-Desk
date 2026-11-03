# Coinbase strategy backtest

Daily candles for 18 coins. Settings picked on data before **2024-07-01**, then judged on **2024-07-01 to 2026-11-02** (854 days), which they never saw. Every buy and sell pays 0.95% (Coinbase US taker fee plus slippage).

Benchmark: an equal-weight basket of all coins returned **-14%** over the test period (worst drop -74%).

## Each strategy, averaged over all coins (test period only)

| Strategy | Avg return | Avg buy-and-hold | Beat holding on | Avg worst drop (vs holding) | Trades per coin |
|---|---|---|---|---|---|
| Moving-average cross | -12% | -18% | 61% of coins | -64% (-80%) | 16 |
| Price above moving average | -42% | -18% | 33% of coins | -76% (-80%) | 63 |
| Breakout (Donchian) | -15% | -18% | 39% of coins | -66% (-80%) | 18 |
| Momentum | -52% | -18% | 22% of coins | -79% (-80%) | 71 |
| RSI dip-buying | +29% | -18% | 78% of coins | -37% (-80%) | 6 |
| Bollinger dip-buying | -12% | -18% | 50% of coins | -45% (-80%) | 13 |

## Every coin and strategy (test period)

| Strategy | Coin | Settings (picked on training data) | Return | Holding | Worst drop | Holding drop | Sharpe | Trades |
|---|---|---|---|---|---|---|---|---|
| Bollinger dip-buying | AAVE | n=50, k=2.5 | +25% | +27% | -40% | -84% | 0.44 | 8 |
| Bollinger dip-buying | ADA | n=50, k=2.5 | +1% | -54% | -63% | -88% | 0.27 | 12 |
| Bollinger dip-buying | ATOM | n=20, k=2.0 | -30% | -79% | -38% | -88% | -0.16 | 27 |
| Bollinger dip-buying | AVAX | n=50, k=2.5 | -25% | -71% | -44% | -89% | -0.09 | 10 |
| Bollinger dip-buying | BCH | n=50, k=2.5 | -41% | -29% | -64% | -71% | -0.36 | 10 |
| Bollinger dip-buying | BTC | n=20, k=2.5 | -4% | +21% | -20% | -53% | 0.02 | 15 |
| Bollinger dip-buying | DOGE | n=50, k=1.5 | -54% | -41% | -68% | -85% | -0.32 | 17 |
| Bollinger dip-buying | DOT | n=50, k=2.5 | -30% | -85% | -50% | -93% | -0.06 | 15 |
| Bollinger dip-buying | ETH | n=20, k=2.0 | -64% | -35% | -64% | -68% | -0.82 | 29 |
| Bollinger dip-buying | LINK | n=50, k=2.5 | -26% | -23% | -52% | -75% | -0.16 | 8 |
| Bollinger dip-buying | LTC | n=50, k=2.5 | +0% | -29% | -28% | -70% | 0.18 | 12 |
| Bollinger dip-buying | NEAR | n=50, k=2.5 | +31% | -27% | -40% | -88% | 0.48 | 8 |
| Bollinger dip-buying | SHIB | n=20, k=2.5 | +17% | -73% | -24% | -87% | 0.39 | 12 |
| Bollinger dip-buying | SOL | n=50, k=2.5 | -12% | -38% | -29% | -76% | -0.11 | 4 |
| Bollinger dip-buying | SUI | n=20, k=2.5 | -33% | +7% | -55% | -88% | -0.36 | 8 |
| Bollinger dip-buying | UNI | n=50, k=2.5 | +16% | -23% | -60% | -87% | 0.39 | 10 |
| Bollinger dip-buying | XLM | n=20, k=2.5 | +1% | +76% | -36% | -74% | 0.12 | 14 |
| Bollinger dip-buying | XRP | n=50, k=2.5 | +8% | +159% | -32% | -72% | 0.26 | 8 |
| Breakout (Donchian) | AAVE | entry=20, exit_=10 | -27% | +27% | -73% | -84% | 0.09 | 28 |
| Breakout (Donchian) | ADA | entry=20, exit_=10 | -68% | -54% | -83% | -88% | -0.72 | 30 |
| Breakout (Donchian) | ATOM | entry=20, exit_=10 | -55% | -79% | -66% | -88% | -0.53 | 20 |
| Breakout (Donchian) | AVAX | entry=55, exit_=10 | -24% | -71% | -63% | -89% | -0.03 | 10 |
| Breakout (Donchian) | BCH | entry=20, exit_=10 | -66% | -29% | -67% | -71% | -0.76 | 24 |
| Breakout (Donchian) | BTC | entry=20, exit_=10 | -9% | +21% | -38% | -53% | -0.01 | 26 |
| Breakout (Donchian) | DOGE | entry=100, exit_=50 | -33% | -41% | -75% | -85% | -0.01 | 6 |
| Breakout (Donchian) | DOT | entry=20, exit_=10 | -46% | -85% | -80% | -93% | -0.31 | 22 |
| Breakout (Donchian) | ETH | entry=100, exit_=50 | -36% | -35% | -51% | -68% | -0.27 | 8 |
| Breakout (Donchian) | LINK | entry=20, exit_=10 | -53% | -23% | -66% | -75% | -0.33 | 30 |
| Breakout (Donchian) | LTC | entry=55, exit_=50 | -54% | -29% | -78% | -70% | -0.32 | 11 |
| Breakout (Donchian) | NEAR | entry=55, exit_=50 | -67% | -27% | -84% | -88% | -0.36 | 11 |
| Breakout (Donchian) | SHIB | entry=20, exit_=10 | -76% | -73% | -81% | -87% | -1.12 | 28 |
| Breakout (Donchian) | SOL | entry=55, exit_=10 | -46% | -38% | -61% | -76% | -0.62 | 18 |
| Breakout (Donchian) | SUI | entry=55, exit_=20 | +15% | +7% | -65% | -88% | 0.38 | 12 |
| Breakout (Donchian) | UNI | entry=20, exit_=10 | +19% | -23% | -64% | -87% | 0.42 | 20 |
| Breakout (Donchian) | XLM | entry=55, exit_=20 | +72% | +76% | -66% | -74% | 0.63 | 10 |
| Breakout (Donchian) | XRP | entry=55, exit_=10 | +286% | +159% | -25% | -72% | 1.41 | 8 |
| Momentum | AAVE | n=14 | -76% | +27% | -84% | -84% | -0.56 | 104 |
| Momentum | ADA | n=30 | -81% | -54% | -92% | -88% | -0.95 | 72 |
| Momentum | ATOM | n=30 | -78% | -79% | -87% | -88% | -1.10 | 64 |
| Momentum | AVAX | n=14 | -73% | -71% | -81% | -89% | -0.65 | 116 |
| Momentum | BCH | n=180 | -72% | -29% | -76% | -71% | -0.77 | 42 |
| Momentum | BTC | n=30 | -54% | +21% | -64% | -53% | -0.93 | 86 |
| Momentum | DOGE | n=30 | -50% | -41% | -82% | -85% | -0.20 | 80 |
| Momentum | DOT | n=90 | -41% | -85% | -75% | -93% | -0.17 | 27 |
| Momentum | ETH | n=180 | -79% | -35% | -80% | -68% | -1.35 | 40 |
| Momentum | LINK | n=30 | -60% | -23% | -80% | -75% | -0.35 | 88 |
| Momentum | LTC | n=90 | +43% | -29% | -39% | -70% | 0.56 | 23 |
| Momentum | NEAR | n=30 | -58% | -27% | -87% | -88% | -0.16 | 68 |
| Momentum | SHIB | n=14 | -82% | -73% | -86% | -87% | -1.06 | 104 |
| Momentum | SOL | n=30 | -50% | -38% | -73% | -76% | -0.35 | 66 |
| Momentum | SUI | n=60 | -26% | +7% | -83% | -88% | 0.15 | 45 |
| Momentum | UNI | n=30 | -3% | -23% | -79% | -87% | 0.33 | 58 |
| Momentum | XLM | n=30 | -55% | +76% | -88% | -74% | -0.09 | 84 |
| Momentum | XRP | n=14 | -32% | +159% | -86% | -72% | 0.03 | 118 |
| Moving-average cross | AAVE | fast=50, slow=200 | +6% | +27% | -63% | -84% | 0.38 | 5 |
| Moving-average cross | ADA | fast=10, slow=50 | -2% | -54% | -65% | -88% | 0.24 | 24 |
| Moving-average cross | ATOM | fast=10, slow=50 | -74% | -79% | -83% | -88% | -0.93 | 32 |
| Moving-average cross | AVAX | fast=10, slow=100 | -17% | -71% | -63% | -89% | 0.16 | 11 |
| Moving-average cross | BCH | fast=20, slow=200 | -48% | -29% | -59% | -71% | -0.40 | 10 |
| Moving-average cross | BTC | fast=10, slow=200 | -20% | +21% | -33% | -53% | -0.14 | 13 |
| Moving-average cross | DOGE | fast=50, slow=200 | -48% | -41% | -78% | -85% | -0.21 | 8 |
| Moving-average cross | DOT | fast=10, slow=50 | -75% | -85% | -83% | -93% | -0.83 | 28 |
| Moving-average cross | ETH | fast=10, slow=200 | -33% | -35% | -42% | -68% | -0.25 | 9 |
| Moving-average cross | LINK | fast=20, slow=100 | +31% | -23% | -54% | -75% | 0.49 | 9 |
| Moving-average cross | LTC | fast=10, slow=200 | -17% | -29% | -55% | -70% | 0.11 | 9 |
| Moving-average cross | NEAR | fast=20, slow=200 | -32% | -27% | -73% | -88% | 0.06 | 11 |
| Moving-average cross | SHIB | fast=20, slow=100 | -51% | -73% | -75% | -87% | -0.47 | 14 |
| Moving-average cross | SOL | fast=10, slow=50 | -15% | -38% | -57% | -76% | 0.10 | 24 |
| Moving-average cross | SUI | fast=10, slow=50 | +12% | +7% | -81% | -88% | 0.41 | 24 |
| Moving-average cross | UNI | fast=10, slow=50 | +128% | -23% | -58% | -87% | 0.85 | 16 |
| Moving-average cross | XLM | fast=10, slow=50 | -18% | +76% | -80% | -74% | 0.22 | 28 |
| Moving-average cross | XRP | fast=20, slow=50 | +64% | +159% | -55% | -72% | 0.64 | 18 |
| Price above moving average | AAVE | n=20 | -88% | +27% | -92% | -84% | -1.02 | 126 |
| Price above moving average | ADA | n=50 | -56% | -54% | -83% | -88% | -0.33 | 66 |
| Price above moving average | ATOM | n=100 | -69% | -79% | -83% | -88% | -0.77 | 44 |
| Price above moving average | AVAX | n=20 | -85% | -71% | -91% | -89% | -1.13 | 116 |
| Price above moving average | BCH | n=200 | -75% | -29% | -80% | -71% | -1.06 | 43 |
| Price above moving average | BTC | n=200 | -13% | +21% | -37% | -53% | -0.04 | 29 |
| Price above moving average | DOGE | n=200 | -37% | -41% | -80% | -85% | -0.09 | 22 |
| Price above moving average | DOT | n=50 | -73% | -85% | -88% | -93% | -0.77 | 56 |
| Price above moving average | ETH | n=200 | -20% | -35% | -43% | -68% | -0.05 | 21 |
| Price above moving average | LINK | n=20 | -71% | -23% | -86% | -75% | -0.55 | 102 |
| Price above moving average | LTC | n=20 | -81% | -29% | -88% | -70% | -1.09 | 114 |
| Price above moving average | NEAR | n=50 | -28% | -27% | -79% | -88% | 0.16 | 46 |
| Price above moving average | SHIB | n=20 | -89% | -73% | -91% | -87% | -1.47 | 120 |
| Price above moving average | SOL | n=50 | -51% | -38% | -69% | -76% | -0.37 | 56 |
| Price above moving average | SUI | n=100 | +18% | +7% | -71% | -88% | 0.43 | 41 |
| Price above moving average | UNI | n=50 | +5% | -23% | -72% | -87% | 0.36 | 48 |
| Price above moving average | XLM | n=50 | -11% | +76% | -79% | -74% | 0.29 | 70 |
| Price above moving average | XRP | n=200 | +73% | +159% | -57% | -72% | 0.67 | 22 |
| RSI dip-buying | AAVE | low=20, high=75 | +93% | +27% | -15% | -84% | 1.16 | 2 |
| RSI dip-buying | ADA | low=25, high=55 | -3% | -54% | -35% | -88% | 0.12 | 6 |
| RSI dip-buying | ATOM | low=20, high=75 | +49% | -79% | -9% | -88% | 1.18 | 2 |
| RSI dip-buying | AVAX | low=30, high=65 | -22% | -71% | -69% | -89% | 0.10 | 13 |
| RSI dip-buying | BCH | low=25, high=65 | -25% | -29% | -50% | -71% | -0.28 | 2 |
| RSI dip-buying | BTC | low=20, high=75 | +14% | +21% | -29% | -53% | 0.38 | 2 |
| RSI dip-buying | DOGE | low=25, high=65 | +3% | -41% | -28% | -85% | 0.18 | 4 |
| RSI dip-buying | DOT | low=20, high=75 | +23% | -85% | -25% | -93% | 0.52 | 2 |
| RSI dip-buying | ETH | low=20, high=65 | +35% | -35% | -13% | -68% | 0.70 | 4 |
| RSI dip-buying | LINK | low=25, high=65 | +61% | -23% | -22% | -75% | 0.78 | 6 |
| RSI dip-buying | LTC | low=30, high=65 | +12% | -29% | -29% | -70% | 0.31 | 8 |
| RSI dip-buying | NEAR | low=35, high=75 | +2% | -27% | -79% | -88% | 0.42 | 8 |
| RSI dip-buying | SHIB | low=20, high=65 | +5% | -73% | -18% | -87% | 0.23 | 2 |
| RSI dip-buying | SOL | low=20, high=75 | +10% | -38% | -36% | -76% | 0.28 | 2 |
| RSI dip-buying | SUI | low=30, high=55 | -26% | +7% | -65% | -88% | 0.01 | 12 |
| RSI dip-buying | UNI | low=25, high=75 | +232% | -23% | -27% | -87% | 1.25 | 6 |
| RSI dip-buying | XLM | low=30, high=65 | +64% | +76% | -52% | -74% | 0.71 | 10 |
| RSI dip-buying | XRP | low=35, high=75 | -9% | +159% | -62% | -72% | 0.21 | 9 |
