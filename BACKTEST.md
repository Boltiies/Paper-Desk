# Coinbase strategy backtest

Daily candles for 18 coins. Settings picked on data before **2024-07-01**, then judged on **2024-07-01 to 2026-11-07** (859 days), which they never saw. Every buy and sell pays 0.95% (Coinbase US taker fee plus slippage).

Benchmark: an equal-weight basket of all coins returned **-16%** over the test period (worst drop -74%).

## Each strategy, averaged over all coins (test period only)

| Strategy | Avg return | Avg buy-and-hold | Beat holding on | Avg worst drop (vs holding) | Trades per coin |
|---|---|---|---|---|---|
| Moving-average cross | -12% | -20% | 61% of coins | -65% (-80%) | 16 |
| Price above moving average | -43% | -20% | 39% of coins | -76% (-80%) | 64 |
| Breakout (Donchian) | -15% | -20% | 44% of coins | -66% (-80%) | 18 |
| Momentum | -52% | -20% | 22% of coins | -79% (-80%) | 72 |
| RSI dip-buying | +28% | -20% | 83% of coins | -37% (-80%) | 6 |
| Bollinger dip-buying | -12% | -20% | 50% of coins | -45% (-80%) | 13 |

## Every coin and strategy (test period)

| Strategy | Coin | Settings (picked on training data) | Return | Holding | Worst drop | Holding drop | Sharpe | Trades |
|---|---|---|---|---|---|---|---|---|
| Bollinger dip-buying | AAVE | n=50, k=2.5 | +25% | +32% | -40% | -84% | 0.44 | 8 |
| Bollinger dip-buying | ADA | n=50, k=2.5 | +1% | -55% | -63% | -88% | 0.27 | 12 |
| Bollinger dip-buying | ATOM | n=20, k=2.0 | -33% | -80% | -38% | -88% | -0.19 | 27 |
| Bollinger dip-buying | AVAX | n=50, k=2.5 | -25% | -72% | -44% | -89% | -0.09 | 10 |
| Bollinger dip-buying | BCH | n=50, k=2.5 | -41% | -36% | -64% | -71% | -0.35 | 10 |
| Bollinger dip-buying | BTC | n=20, k=2.5 | -0% | +19% | -20% | -53% | 0.10 | 16 |
| Bollinger dip-buying | DOGE | n=50, k=1.5 | -55% | -43% | -68% | -85% | -0.34 | 17 |
| Bollinger dip-buying | DOT | n=50, k=2.5 | -33% | -86% | -50% | -93% | -0.10 | 15 |
| Bollinger dip-buying | ETH | n=20, k=2.0 | -62% | -36% | -64% | -68% | -0.74 | 30 |
| Bollinger dip-buying | LINK | n=50, k=2.5 | -26% | -25% | -52% | -75% | -0.16 | 8 |
| Bollinger dip-buying | LTC | n=50, k=2.5 | +0% | -30% | -28% | -70% | 0.17 | 12 |
| Bollinger dip-buying | NEAR | n=50, k=2.5 | +31% | -30% | -40% | -88% | 0.48 | 8 |
| Bollinger dip-buying | SHIB | n=20, k=2.5 | +17% | -74% | -24% | -87% | 0.39 | 12 |
| Bollinger dip-buying | SOL | n=50, k=2.5 | -12% | -39% | -29% | -76% | -0.11 | 4 |
| Bollinger dip-buying | SUI | n=20, k=2.5 | -33% | +5% | -55% | -88% | -0.36 | 8 |
| Bollinger dip-buying | UNI | n=50, k=2.5 | +16% | -22% | -60% | -87% | 0.39 | 10 |
| Bollinger dip-buying | XLM | n=20, k=2.5 | +1% | +64% | -36% | -74% | 0.12 | 14 |
| Bollinger dip-buying | XRP | n=50, k=2.5 | +8% | +142% | -32% | -72% | 0.26 | 8 |
| Breakout (Donchian) | AAVE | entry=20, exit_=10 | -27% | +32% | -73% | -84% | 0.09 | 28 |
| Breakout (Donchian) | ADA | entry=20, exit_=10 | -68% | -55% | -83% | -88% | -0.72 | 30 |
| Breakout (Donchian) | ATOM | entry=20, exit_=10 | -55% | -80% | -66% | -88% | -0.53 | 20 |
| Breakout (Donchian) | AVAX | entry=55, exit_=10 | -24% | -72% | -63% | -89% | -0.03 | 10 |
| Breakout (Donchian) | BCH | entry=20, exit_=10 | -66% | -36% | -67% | -71% | -0.76 | 24 |
| Breakout (Donchian) | BTC | entry=20, exit_=10 | -9% | +19% | -38% | -53% | -0.01 | 26 |
| Breakout (Donchian) | DOGE | entry=100, exit_=50 | -33% | -43% | -75% | -85% | -0.01 | 6 |
| Breakout (Donchian) | DOT | entry=20, exit_=10 | -46% | -86% | -80% | -93% | -0.31 | 22 |
| Breakout (Donchian) | ETH | entry=100, exit_=50 | -36% | -36% | -51% | -68% | -0.27 | 8 |
| Breakout (Donchian) | LINK | entry=20, exit_=10 | -53% | -25% | -66% | -75% | -0.33 | 30 |
| Breakout (Donchian) | LTC | entry=55, exit_=50 | -55% | -30% | -78% | -70% | -0.33 | 11 |
| Breakout (Donchian) | NEAR | entry=55, exit_=50 | -68% | -30% | -84% | -88% | -0.37 | 11 |
| Breakout (Donchian) | SHIB | entry=20, exit_=10 | -76% | -74% | -81% | -87% | -1.11 | 28 |
| Breakout (Donchian) | SOL | entry=55, exit_=10 | -46% | -39% | -61% | -76% | -0.62 | 18 |
| Breakout (Donchian) | SUI | entry=55, exit_=20 | +15% | +5% | -65% | -88% | 0.38 | 12 |
| Breakout (Donchian) | UNI | entry=20, exit_=10 | +19% | -22% | -64% | -87% | 0.42 | 20 |
| Breakout (Donchian) | XLM | entry=55, exit_=20 | +72% | +64% | -66% | -74% | 0.63 | 10 |
| Breakout (Donchian) | XRP | entry=55, exit_=10 | +286% | +142% | -25% | -72% | 1.40 | 8 |
| Momentum | AAVE | n=14 | -76% | +32% | -84% | -84% | -0.55 | 104 |
| Momentum | ADA | n=30 | -81% | -55% | -92% | -88% | -0.94 | 72 |
| Momentum | ATOM | n=30 | -78% | -80% | -87% | -88% | -1.10 | 64 |
| Momentum | AVAX | n=14 | -73% | -72% | -81% | -89% | -0.64 | 116 |
| Momentum | BCH | n=180 | -72% | -36% | -76% | -71% | -0.77 | 42 |
| Momentum | BTC | n=30 | -54% | +19% | -64% | -53% | -0.93 | 86 |
| Momentum | DOGE | n=30 | -50% | -43% | -82% | -85% | -0.20 | 80 |
| Momentum | DOT | n=90 | -44% | -86% | -75% | -93% | -0.21 | 27 |
| Momentum | ETH | n=180 | -81% | -36% | -81% | -68% | -1.43 | 42 |
| Momentum | LINK | n=30 | -60% | -25% | -80% | -75% | -0.35 | 88 |
| Momentum | LTC | n=90 | +40% | -30% | -39% | -70% | 0.53 | 23 |
| Momentum | NEAR | n=30 | -58% | -30% | -87% | -88% | -0.16 | 68 |
| Momentum | SHIB | n=14 | -82% | -74% | -86% | -87% | -1.06 | 104 |
| Momentum | SOL | n=30 | -50% | -39% | -73% | -76% | -0.35 | 66 |
| Momentum | SUI | n=60 | -27% | +5% | -83% | -88% | 0.14 | 45 |
| Momentum | UNI | n=30 | -3% | -22% | -79% | -87% | 0.33 | 58 |
| Momentum | XLM | n=30 | -55% | +64% | -88% | -74% | -0.09 | 84 |
| Momentum | XRP | n=14 | -32% | +142% | -86% | -72% | 0.03 | 118 |
| Moving-average cross | AAVE | fast=50, slow=200 | +11% | +32% | -63% | -84% | 0.41 | 5 |
| Moving-average cross | ADA | fast=10, slow=50 | -2% | -55% | -65% | -88% | 0.24 | 24 |
| Moving-average cross | ATOM | fast=10, slow=50 | -74% | -80% | -83% | -88% | -0.93 | 32 |
| Moving-average cross | AVAX | fast=10, slow=100 | -19% | -72% | -63% | -89% | 0.14 | 11 |
| Moving-average cross | BCH | fast=20, slow=200 | -53% | -36% | -61% | -71% | -0.48 | 11 |
| Moving-average cross | BTC | fast=10, slow=200 | -21% | +19% | -33% | -53% | -0.15 | 13 |
| Moving-average cross | DOGE | fast=50, slow=200 | -48% | -43% | -78% | -85% | -0.21 | 8 |
| Moving-average cross | DOT | fast=10, slow=50 | -75% | -86% | -83% | -93% | -0.83 | 28 |
| Moving-average cross | ETH | fast=10, slow=200 | -33% | -36% | -42% | -68% | -0.24 | 9 |
| Moving-average cross | LINK | fast=20, slow=100 | +27% | -25% | -54% | -75% | 0.47 | 9 |
| Moving-average cross | LTC | fast=10, slow=200 | -19% | -30% | -55% | -70% | 0.08 | 9 |
| Moving-average cross | NEAR | fast=20, slow=200 | -34% | -30% | -73% | -88% | 0.04 | 11 |
| Moving-average cross | SHIB | fast=20, slow=100 | -51% | -74% | -75% | -87% | -0.47 | 14 |
| Moving-average cross | SOL | fast=10, slow=50 | -15% | -39% | -57% | -76% | 0.10 | 24 |
| Moving-average cross | SUI | fast=10, slow=50 | +12% | +5% | -81% | -88% | 0.41 | 24 |
| Moving-average cross | UNI | fast=10, slow=50 | +128% | -22% | -58% | -87% | 0.84 | 16 |
| Moving-average cross | XLM | fast=10, slow=50 | -18% | +64% | -80% | -74% | 0.22 | 28 |
| Moving-average cross | XRP | fast=20, slow=50 | +64% | +142% | -55% | -72% | 0.64 | 18 |
| Price above moving average | AAVE | n=20 | -88% | +32% | -92% | -84% | -1.02 | 126 |
| Price above moving average | ADA | n=50 | -56% | -55% | -83% | -88% | -0.33 | 66 |
| Price above moving average | ATOM | n=100 | -69% | -80% | -83% | -88% | -0.77 | 44 |
| Price above moving average | AVAX | n=20 | -85% | -72% | -91% | -89% | -1.13 | 116 |
| Price above moving average | BCH | n=200 | -77% | -36% | -81% | -71% | -1.12 | 46 |
| Price above moving average | BTC | n=200 | -14% | +19% | -37% | -53% | -0.05 | 29 |
| Price above moving average | DOGE | n=200 | -37% | -43% | -80% | -85% | -0.09 | 22 |
| Price above moving average | DOT | n=50 | -73% | -86% | -88% | -93% | -0.77 | 56 |
| Price above moving average | ETH | n=200 | -20% | -36% | -43% | -68% | -0.05 | 21 |
| Price above moving average | LINK | n=20 | -71% | -25% | -86% | -75% | -0.55 | 102 |
| Price above moving average | LTC | n=20 | -81% | -30% | -88% | -70% | -1.09 | 114 |
| Price above moving average | NEAR | n=50 | -28% | -30% | -79% | -88% | 0.16 | 46 |
| Price above moving average | SHIB | n=20 | -89% | -74% | -91% | -87% | -1.46 | 120 |
| Price above moving average | SOL | n=50 | -51% | -39% | -69% | -76% | -0.37 | 56 |
| Price above moving average | SUI | n=100 | +13% | +5% | -71% | -88% | 0.40 | 42 |
| Price above moving average | UNI | n=50 | +5% | -22% | -72% | -87% | 0.36 | 48 |
| Price above moving average | XLM | n=50 | -11% | +64% | -79% | -74% | 0.28 | 70 |
| Price above moving average | XRP | n=200 | +60% | +142% | -60% | -72% | 0.62 | 24 |
| RSI dip-buying | AAVE | low=20, high=75 | +93% | +32% | -15% | -84% | 1.15 | 2 |
| RSI dip-buying | ADA | low=25, high=55 | -3% | -55% | -35% | -88% | 0.12 | 6 |
| RSI dip-buying | ATOM | low=20, high=75 | +49% | -80% | -9% | -88% | 1.18 | 2 |
| RSI dip-buying | AVAX | low=30, high=65 | -24% | -72% | -69% | -89% | 0.09 | 13 |
| RSI dip-buying | BCH | low=25, high=65 | -25% | -36% | -50% | -71% | -0.28 | 2 |
| RSI dip-buying | BTC | low=20, high=75 | +14% | +19% | -29% | -53% | 0.38 | 2 |
| RSI dip-buying | DOGE | low=25, high=65 | +3% | -43% | -28% | -85% | 0.18 | 4 |
| RSI dip-buying | DOT | low=20, high=75 | +23% | -86% | -25% | -93% | 0.52 | 2 |
| RSI dip-buying | ETH | low=20, high=65 | +35% | -36% | -13% | -68% | 0.70 | 4 |
| RSI dip-buying | LINK | low=25, high=65 | +61% | -25% | -22% | -75% | 0.78 | 6 |
| RSI dip-buying | LTC | low=30, high=65 | +12% | -30% | -29% | -70% | 0.31 | 8 |
| RSI dip-buying | NEAR | low=35, high=75 | +2% | -30% | -79% | -88% | 0.42 | 8 |
| RSI dip-buying | SHIB | low=20, high=65 | +5% | -74% | -18% | -87% | 0.22 | 2 |
| RSI dip-buying | SOL | low=20, high=75 | +10% | -39% | -36% | -76% | 0.28 | 2 |
| RSI dip-buying | SUI | low=30, high=55 | -26% | +5% | -65% | -88% | 0.01 | 12 |
| RSI dip-buying | UNI | low=25, high=75 | +232% | -22% | -27% | -87% | 1.24 | 6 |
| RSI dip-buying | XLM | low=30, high=65 | +64% | +64% | -52% | -74% | 0.71 | 10 |
| RSI dip-buying | XRP | low=35, high=75 | -16% | +142% | -62% | -72% | 0.16 | 9 |
