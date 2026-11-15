# Coinbase strategy backtest

Daily candles for 18 coins. Settings picked on data before **2024-07-01**, then judged on **2024-07-01 to 2026-11-14** (866 days), which they never saw. Every buy and sell pays 0.95% (Coinbase US taker fee plus slippage).

Benchmark: an equal-weight basket of all coins returned **-32%** over the test period (worst drop -74%).

## Each strategy, averaged over all coins (test period only)

| Strategy | Avg return | Avg buy-and-hold | Beat holding on | Avg worst drop (vs holding) | Trades per coin |
|---|---|---|---|---|---|
| Moving-average cross | -16% | -35% | 67% of coins | -66% (-80%) | 17 |
| Price above moving average | -44% | -35% | 50% of coins | -76% (-80%) | 64 |
| Breakout (Donchian) | -15% | -35% | 61% of coins | -66% (-80%) | 18 |
| Momentum | -55% | -35% | 39% of coins | -80% (-80%) | 72 |
| RSI dip-buying | +25% | -35% | 89% of coins | -37% (-80%) | 6 |
| Bollinger dip-buying | -15% | -35% | 67% of coins | -45% (-80%) | 13 |

## Every coin and strategy (test period)

| Strategy | Coin | Settings (picked on training data) | Return | Holding | Worst drop | Holding drop | Sharpe | Trades |
|---|---|---|---|---|---|---|---|---|
| Bollinger dip-buying | AAVE | n=50, k=2.5 | +25% | +1% | -40% | -84% | 0.44 | 8 |
| Bollinger dip-buying | ADA | n=50, k=2.5 | +1% | -64% | -63% | -88% | 0.27 | 12 |
| Bollinger dip-buying | ATOM | n=20, k=2.0 | -38% | -82% | -38% | -88% | -0.27 | 27 |
| Bollinger dip-buying | AVAX | n=50, k=2.5 | -25% | -76% | -44% | -89% | -0.09 | 10 |
| Bollinger dip-buying | BCH | n=50, k=2.5 | -41% | -48% | -64% | -71% | -0.35 | 10 |
| Bollinger dip-buying | BTC | n=20, k=2.5 | -7% | +1% | -20% | -53% | -0.04 | 17 |
| Bollinger dip-buying | DOGE | n=50, k=1.5 | -64% | -54% | -75% | -88% | -0.50 | 17 |
| Bollinger dip-buying | DOT | n=50, k=2.5 | -47% | -89% | -50% | -93% | -0.28 | 15 |
| Bollinger dip-buying | ETH | n=20, k=2.0 | -68% | -49% | -68% | -68% | -0.92 | 31 |
| Bollinger dip-buying | LINK | n=50, k=2.5 | -26% | -39% | -52% | -75% | -0.16 | 8 |
| Bollinger dip-buying | LTC | n=50, k=2.5 | +0% | -41% | -28% | -70% | 0.17 | 12 |
| Bollinger dip-buying | NEAR | n=50, k=2.5 | +31% | -43% | -40% | -88% | 0.48 | 8 |
| Bollinger dip-buying | SHIB | n=20, k=2.5 | +17% | -78% | -24% | -88% | 0.39 | 12 |
| Bollinger dip-buying | SOL | n=50, k=2.5 | -12% | -52% | -29% | -76% | -0.11 | 4 |
| Bollinger dip-buying | SUI | n=20, k=2.5 | -33% | -14% | -55% | -88% | -0.36 | 8 |
| Bollinger dip-buying | UNI | n=50, k=2.5 | +16% | -47% | -60% | -87% | 0.38 | 10 |
| Bollinger dip-buying | XLM | n=20, k=2.5 | +1% | +47% | -36% | -76% | 0.12 | 14 |
| Bollinger dip-buying | XRP | n=50, k=2.5 | +8% | +90% | -32% | -74% | 0.26 | 8 |
| Breakout (Donchian) | AAVE | entry=20, exit_=10 | -27% | +1% | -73% | -84% | 0.09 | 28 |
| Breakout (Donchian) | ADA | entry=20, exit_=10 | -68% | -64% | -83% | -88% | -0.71 | 30 |
| Breakout (Donchian) | ATOM | entry=20, exit_=10 | -55% | -82% | -66% | -88% | -0.53 | 20 |
| Breakout (Donchian) | AVAX | entry=55, exit_=10 | -24% | -76% | -63% | -89% | -0.03 | 10 |
| Breakout (Donchian) | BCH | entry=20, exit_=10 | -66% | -48% | -67% | -71% | -0.76 | 24 |
| Breakout (Donchian) | BTC | entry=20, exit_=10 | -9% | +1% | -38% | -53% | -0.01 | 26 |
| Breakout (Donchian) | DOGE | entry=100, exit_=50 | -33% | -54% | -75% | -88% | -0.01 | 6 |
| Breakout (Donchian) | DOT | entry=20, exit_=10 | -46% | -89% | -80% | -93% | -0.31 | 22 |
| Breakout (Donchian) | ETH | entry=100, exit_=50 | -36% | -49% | -51% | -68% | -0.27 | 8 |
| Breakout (Donchian) | LINK | entry=20, exit_=10 | -53% | -39% | -66% | -75% | -0.33 | 30 |
| Breakout (Donchian) | LTC | entry=55, exit_=50 | -57% | -41% | -78% | -70% | -0.37 | 12 |
| Breakout (Donchian) | NEAR | entry=55, exit_=50 | -71% | -43% | -84% | -88% | -0.43 | 12 |
| Breakout (Donchian) | SHIB | entry=20, exit_=10 | -76% | -78% | -81% | -88% | -1.11 | 28 |
| Breakout (Donchian) | SOL | entry=55, exit_=10 | -46% | -52% | -61% | -76% | -0.62 | 18 |
| Breakout (Donchian) | SUI | entry=55, exit_=20 | +15% | -14% | -65% | -88% | 0.38 | 12 |
| Breakout (Donchian) | UNI | entry=20, exit_=10 | +19% | -47% | -64% | -87% | 0.41 | 20 |
| Breakout (Donchian) | XLM | entry=55, exit_=20 | +72% | +47% | -66% | -76% | 0.63 | 10 |
| Breakout (Donchian) | XRP | entry=55, exit_=10 | +286% | +90% | -25% | -74% | 1.40 | 8 |
| Momentum | AAVE | n=14 | -76% | +1% | -84% | -84% | -0.55 | 104 |
| Momentum | ADA | n=30 | -81% | -64% | -92% | -88% | -0.94 | 72 |
| Momentum | ATOM | n=30 | -78% | -82% | -87% | -88% | -1.09 | 64 |
| Momentum | AVAX | n=14 | -74% | -76% | -81% | -89% | -0.67 | 118 |
| Momentum | BCH | n=180 | -72% | -48% | -76% | -71% | -0.76 | 42 |
| Momentum | BTC | n=30 | -54% | +1% | -64% | -53% | -0.93 | 86 |
| Momentum | DOGE | n=30 | -50% | -54% | -82% | -88% | -0.20 | 80 |
| Momentum | DOT | n=90 | -56% | -89% | -81% | -93% | -0.38 | 27 |
| Momentum | ETH | n=180 | -81% | -49% | -81% | -68% | -1.43 | 42 |
| Momentum | LINK | n=30 | -60% | -39% | -80% | -75% | -0.35 | 88 |
| Momentum | LTC | n=90 | +19% | -41% | -45% | -70% | 0.40 | 23 |
| Momentum | NEAR | n=30 | -58% | -43% | -87% | -88% | -0.15 | 68 |
| Momentum | SHIB | n=14 | -82% | -78% | -86% | -88% | -1.05 | 104 |
| Momentum | SOL | n=30 | -50% | -52% | -73% | -76% | -0.35 | 66 |
| Momentum | SUI | n=60 | -40% | -14% | -85% | -88% | 0.02 | 45 |
| Momentum | UNI | n=30 | -11% | -47% | -79% | -87% | 0.28 | 60 |
| Momentum | XLM | n=30 | -55% | +47% | -88% | -76% | -0.09 | 84 |
| Momentum | XRP | n=14 | -32% | +90% | -86% | -74% | 0.03 | 118 |
| Moving-average cross | AAVE | fast=50, slow=200 | -16% | +1% | -68% | -84% | 0.25 | 5 |
| Moving-average cross | ADA | fast=10, slow=50 | -2% | -64% | -65% | -88% | 0.24 | 24 |
| Moving-average cross | ATOM | fast=10, slow=50 | -74% | -82% | -83% | -88% | -0.92 | 32 |
| Moving-average cross | AVAX | fast=10, slow=100 | -20% | -76% | -63% | -89% | 0.14 | 12 |
| Moving-average cross | BCH | fast=20, slow=200 | -55% | -48% | -63% | -71% | -0.53 | 12 |
| Moving-average cross | BTC | fast=10, slow=200 | -33% | +1% | -37% | -53% | -0.36 | 13 |
| Moving-average cross | DOGE | fast=50, slow=200 | -48% | -54% | -78% | -88% | -0.21 | 8 |
| Moving-average cross | DOT | fast=10, slow=50 | -75% | -89% | -83% | -93% | -0.83 | 28 |
| Moving-average cross | ETH | fast=10, slow=200 | -43% | -49% | -50% | -68% | -0.41 | 10 |
| Moving-average cross | LINK | fast=20, slow=100 | +26% | -39% | -54% | -75% | 0.46 | 10 |
| Moving-average cross | LTC | fast=10, slow=200 | -23% | -41% | -57% | -70% | 0.04 | 10 |
| Moving-average cross | NEAR | fast=20, slow=200 | -47% | -43% | -73% | -88% | -0.09 | 11 |
| Moving-average cross | SHIB | fast=20, slow=100 | -51% | -78% | -75% | -88% | -0.47 | 14 |
| Moving-average cross | SOL | fast=10, slow=50 | -15% | -52% | -57% | -76% | 0.10 | 24 |
| Moving-average cross | SUI | fast=10, slow=50 | +12% | -14% | -81% | -88% | 0.41 | 24 |
| Moving-average cross | UNI | fast=10, slow=50 | +128% | -47% | -58% | -87% | 0.84 | 16 |
| Moving-average cross | XLM | fast=10, slow=50 | -18% | +47% | -80% | -76% | 0.22 | 28 |
| Moving-average cross | XRP | fast=20, slow=50 | +64% | +90% | -55% | -74% | 0.64 | 18 |
| Price above moving average | AAVE | n=20 | -88% | +1% | -92% | -84% | -1.01 | 126 |
| Price above moving average | ADA | n=50 | -56% | -64% | -83% | -88% | -0.33 | 66 |
| Price above moving average | ATOM | n=100 | -69% | -82% | -83% | -88% | -0.76 | 44 |
| Price above moving average | AVAX | n=20 | -85% | -76% | -91% | -89% | -1.13 | 116 |
| Price above moving average | BCH | n=200 | -77% | -48% | -81% | -71% | -1.11 | 46 |
| Price above moving average | BTC | n=200 | -20% | +1% | -37% | -53% | -0.14 | 30 |
| Price above moving average | DOGE | n=200 | -37% | -54% | -80% | -88% | -0.08 | 22 |
| Price above moving average | DOT | n=50 | -73% | -89% | -88% | -93% | -0.77 | 56 |
| Price above moving average | ETH | n=200 | -25% | -49% | -46% | -68% | -0.11 | 22 |
| Price above moving average | LINK | n=20 | -71% | -39% | -86% | -75% | -0.54 | 102 |
| Price above moving average | LTC | n=20 | -81% | -41% | -88% | -70% | -1.08 | 114 |
| Price above moving average | NEAR | n=50 | -28% | -43% | -79% | -88% | 0.16 | 46 |
| Price above moving average | SHIB | n=20 | -89% | -78% | -91% | -88% | -1.46 | 120 |
| Price above moving average | SOL | n=50 | -51% | -52% | -69% | -76% | -0.37 | 56 |
| Price above moving average | SUI | n=100 | +13% | -14% | -71% | -88% | 0.40 | 42 |
| Price above moving average | UNI | n=50 | +5% | -47% | -72% | -87% | 0.36 | 48 |
| Price above moving average | XLM | n=50 | -11% | +47% | -79% | -76% | 0.28 | 70 |
| Price above moving average | XRP | n=200 | +60% | +90% | -60% | -74% | 0.62 | 24 |
| RSI dip-buying | AAVE | low=20, high=75 | +93% | +1% | -15% | -84% | 1.15 | 2 |
| RSI dip-buying | ADA | low=25, high=55 | -3% | -64% | -35% | -88% | 0.12 | 6 |
| RSI dip-buying | ATOM | low=20, high=75 | +49% | -82% | -9% | -88% | 1.17 | 2 |
| RSI dip-buying | AVAX | low=30, high=65 | -34% | -76% | -69% | -89% | -0.01 | 13 |
| RSI dip-buying | BCH | low=25, high=65 | -25% | -48% | -50% | -71% | -0.28 | 2 |
| RSI dip-buying | BTC | low=20, high=75 | +14% | +1% | -29% | -53% | 0.38 | 2 |
| RSI dip-buying | DOGE | low=25, high=65 | +3% | -54% | -28% | -88% | 0.18 | 4 |
| RSI dip-buying | DOT | low=20, high=75 | +23% | -89% | -25% | -93% | 0.51 | 2 |
| RSI dip-buying | ETH | low=20, high=65 | +35% | -49% | -13% | -68% | 0.70 | 4 |
| RSI dip-buying | LINK | low=25, high=65 | +61% | -39% | -22% | -75% | 0.78 | 6 |
| RSI dip-buying | LTC | low=30, high=65 | +12% | -41% | -29% | -70% | 0.31 | 8 |
| RSI dip-buying | NEAR | low=35, high=75 | +2% | -43% | -79% | -88% | 0.42 | 8 |
| RSI dip-buying | SHIB | low=20, high=65 | +5% | -78% | -18% | -88% | 0.22 | 2 |
| RSI dip-buying | SOL | low=20, high=75 | -2% | -52% | -36% | -76% | 0.11 | 3 |
| RSI dip-buying | SUI | low=30, high=55 | -26% | -14% | -65% | -88% | 0.01 | 12 |
| RSI dip-buying | UNI | low=25, high=75 | +232% | -47% | -27% | -87% | 1.24 | 6 |
| RSI dip-buying | XLM | low=30, high=65 | +51% | +47% | -52% | -76% | 0.62 | 11 |
| RSI dip-buying | XRP | low=35, high=75 | -34% | +90% | -67% | -74% | -0.01 | 9 |
