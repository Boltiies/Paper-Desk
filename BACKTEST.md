# Coinbase strategy backtest

Daily candles for 18 coins. Settings picked on data before **2024-07-01**, then judged on **2024-07-01 to 2026-11-21** (873 days), which they never saw. Every buy and sell pays 0.95% (Coinbase US taker fee plus slippage).

Benchmark: an equal-weight basket of all coins returned **-35%** over the test period (worst drop -74%).

## Each strategy, averaged over all coins (test period only)

| Strategy | Avg return | Avg buy-and-hold | Beat holding on | Avg worst drop (vs holding) | Trades per coin |
|---|---|---|---|---|---|
| Moving-average cross | -16% | -38% | 67% of coins | -66% (-81%) | 17 |
| Price above moving average | -44% | -38% | 50% of coins | -76% (-81%) | 64 |
| Breakout (Donchian) | -15% | -38% | 61% of coins | -66% (-81%) | 18 |
| Momentum | -55% | -38% | 39% of coins | -80% (-81%) | 72 |
| RSI dip-buying | +21% | -38% | 89% of coins | -37% (-81%) | 6 |
| Bollinger dip-buying | -17% | -38% | 67% of coins | -46% (-81%) | 13 |

## Every coin and strategy (test period)

| Strategy | Coin | Settings (picked on training data) | Return | Holding | Worst drop | Holding drop | Sharpe | Trades |
|---|---|---|---|---|---|---|---|---|
| Bollinger dip-buying | AAVE | n=50, k=2.5 | +25% | -2% | -40% | -84% | 0.44 | 8 |
| Bollinger dip-buying | ADA | n=50, k=2.5 | +1% | -65% | -63% | -88% | 0.27 | 12 |
| Bollinger dip-buying | ATOM | n=20, k=2.0 | -43% | -83% | -43% | -89% | -0.34 | 27 |
| Bollinger dip-buying | AVAX | n=50, k=2.5 | -25% | -77% | -44% | -89% | -0.09 | 10 |
| Bollinger dip-buying | BCH | n=50, k=2.5 | -42% | -49% | -64% | -71% | -0.36 | 11 |
| Bollinger dip-buying | BTC | n=20, k=2.5 | -13% | -5% | -26% | -53% | -0.15 | 17 |
| Bollinger dip-buying | DOGE | n=50, k=1.5 | -66% | -56% | -76% | -88% | -0.52 | 17 |
| Bollinger dip-buying | DOT | n=50, k=2.5 | -51% | -90% | -54% | -94% | -0.34 | 15 |
| Bollinger dip-buying | ETH | n=20, k=2.0 | -70% | -52% | -71% | -68% | -0.94 | 31 |
| Bollinger dip-buying | LINK | n=50, k=2.5 | -26% | -41% | -52% | -75% | -0.16 | 8 |
| Bollinger dip-buying | LTC | n=50, k=2.5 | +0% | -47% | -28% | -71% | 0.17 | 12 |
| Bollinger dip-buying | NEAR | n=50, k=2.5 | +31% | -46% | -40% | -88% | 0.48 | 8 |
| Bollinger dip-buying | SHIB | n=20, k=2.5 | +10% | -79% | -24% | -89% | 0.28 | 13 |
| Bollinger dip-buying | SOL | n=50, k=2.5 | -13% | -53% | -29% | -76% | -0.12 | 5 |
| Bollinger dip-buying | SUI | n=20, k=2.5 | -39% | -21% | -55% | -88% | -0.45 | 9 |
| Bollinger dip-buying | UNI | n=50, k=2.5 | +11% | -49% | -60% | -87% | 0.36 | 11 |
| Bollinger dip-buying | XLM | n=20, k=2.5 | +1% | +40% | -36% | -77% | 0.12 | 14 |
| Bollinger dip-buying | XRP | n=50, k=2.5 | +9% | +93% | -32% | -74% | 0.27 | 9 |
| Breakout (Donchian) | AAVE | entry=20, exit_=10 | -27% | -2% | -73% | -84% | 0.08 | 28 |
| Breakout (Donchian) | ADA | entry=20, exit_=10 | -68% | -65% | -83% | -88% | -0.71 | 30 |
| Breakout (Donchian) | ATOM | entry=20, exit_=10 | -55% | -83% | -66% | -89% | -0.52 | 20 |
| Breakout (Donchian) | AVAX | entry=55, exit_=10 | -24% | -77% | -63% | -89% | -0.03 | 10 |
| Breakout (Donchian) | BCH | entry=20, exit_=10 | -66% | -49% | -67% | -71% | -0.75 | 24 |
| Breakout (Donchian) | BTC | entry=20, exit_=10 | -9% | -5% | -38% | -53% | -0.01 | 26 |
| Breakout (Donchian) | DOGE | entry=100, exit_=50 | -33% | -56% | -75% | -88% | -0.01 | 6 |
| Breakout (Donchian) | DOT | entry=20, exit_=10 | -46% | -90% | -80% | -94% | -0.31 | 22 |
| Breakout (Donchian) | ETH | entry=100, exit_=50 | -36% | -52% | -51% | -68% | -0.27 | 8 |
| Breakout (Donchian) | LINK | entry=20, exit_=10 | -53% | -41% | -66% | -75% | -0.32 | 30 |
| Breakout (Donchian) | LTC | entry=55, exit_=50 | -57% | -47% | -78% | -71% | -0.37 | 12 |
| Breakout (Donchian) | NEAR | entry=55, exit_=50 | -71% | -46% | -84% | -88% | -0.43 | 12 |
| Breakout (Donchian) | SHIB | entry=20, exit_=10 | -76% | -79% | -81% | -89% | -1.11 | 28 |
| Breakout (Donchian) | SOL | entry=55, exit_=10 | -46% | -53% | -61% | -76% | -0.62 | 18 |
| Breakout (Donchian) | SUI | entry=55, exit_=20 | +15% | -21% | -65% | -88% | 0.38 | 12 |
| Breakout (Donchian) | UNI | entry=20, exit_=10 | +19% | -49% | -64% | -87% | 0.41 | 20 |
| Breakout (Donchian) | XLM | entry=55, exit_=20 | +72% | +40% | -66% | -77% | 0.63 | 10 |
| Breakout (Donchian) | XRP | entry=55, exit_=10 | +286% | +93% | -25% | -74% | 1.39 | 8 |
| Momentum | AAVE | n=14 | -76% | -2% | -84% | -84% | -0.55 | 104 |
| Momentum | ADA | n=30 | -81% | -65% | -92% | -88% | -0.94 | 72 |
| Momentum | ATOM | n=30 | -78% | -83% | -87% | -89% | -1.09 | 64 |
| Momentum | AVAX | n=14 | -74% | -77% | -81% | -89% | -0.66 | 118 |
| Momentum | BCH | n=180 | -72% | -49% | -76% | -71% | -0.76 | 42 |
| Momentum | BTC | n=30 | -54% | -5% | -64% | -53% | -0.92 | 86 |
| Momentum | DOGE | n=30 | -50% | -56% | -82% | -88% | -0.20 | 80 |
| Momentum | DOT | n=90 | -56% | -90% | -81% | -94% | -0.39 | 28 |
| Momentum | ETH | n=180 | -81% | -52% | -81% | -68% | -1.42 | 42 |
| Momentum | LINK | n=30 | -60% | -41% | -80% | -75% | -0.35 | 88 |
| Momentum | LTC | n=90 | +20% | -47% | -45% | -71% | 0.41 | 24 |
| Momentum | NEAR | n=30 | -58% | -46% | -87% | -88% | -0.15 | 68 |
| Momentum | SHIB | n=14 | -82% | -79% | -86% | -89% | -1.05 | 104 |
| Momentum | SOL | n=30 | -50% | -53% | -73% | -76% | -0.35 | 66 |
| Momentum | SUI | n=60 | -39% | -21% | -85% | -88% | 0.03 | 46 |
| Momentum | UNI | n=30 | -11% | -49% | -79% | -87% | 0.28 | 60 |
| Momentum | XLM | n=30 | -55% | +40% | -88% | -77% | -0.09 | 84 |
| Momentum | XRP | n=14 | -32% | +93% | -86% | -74% | 0.03 | 118 |
| Moving-average cross | AAVE | fast=50, slow=200 | -18% | -2% | -69% | -84% | 0.23 | 5 |
| Moving-average cross | ADA | fast=10, slow=50 | -2% | -65% | -65% | -88% | 0.24 | 24 |
| Moving-average cross | ATOM | fast=10, slow=50 | -74% | -83% | -83% | -89% | -0.92 | 32 |
| Moving-average cross | AVAX | fast=10, slow=100 | -20% | -77% | -63% | -89% | 0.13 | 12 |
| Moving-average cross | BCH | fast=20, slow=200 | -55% | -49% | -63% | -71% | -0.53 | 12 |
| Moving-average cross | BTC | fast=10, slow=200 | -33% | -5% | -38% | -53% | -0.38 | 14 |
| Moving-average cross | DOGE | fast=50, slow=200 | -48% | -56% | -78% | -88% | -0.21 | 8 |
| Moving-average cross | DOT | fast=10, slow=50 | -75% | -90% | -83% | -94% | -0.82 | 28 |
| Moving-average cross | ETH | fast=10, slow=200 | -43% | -52% | -50% | -68% | -0.40 | 10 |
| Moving-average cross | LINK | fast=20, slow=100 | +26% | -41% | -54% | -75% | 0.46 | 10 |
| Moving-average cross | LTC | fast=10, slow=200 | -23% | -47% | -57% | -71% | 0.04 | 10 |
| Moving-average cross | NEAR | fast=20, slow=200 | -49% | -46% | -73% | -88% | -0.11 | 11 |
| Moving-average cross | SHIB | fast=20, slow=100 | -51% | -79% | -75% | -89% | -0.46 | 14 |
| Moving-average cross | SOL | fast=10, slow=50 | -15% | -53% | -57% | -76% | 0.10 | 24 |
| Moving-average cross | SUI | fast=10, slow=50 | +12% | -21% | -81% | -88% | 0.41 | 24 |
| Moving-average cross | UNI | fast=10, slow=50 | +128% | -49% | -58% | -87% | 0.84 | 16 |
| Moving-average cross | XLM | fast=10, slow=50 | -18% | +40% | -80% | -77% | 0.22 | 28 |
| Moving-average cross | XRP | fast=20, slow=50 | +64% | +93% | -55% | -74% | 0.64 | 18 |
| Price above moving average | AAVE | n=20 | -88% | -2% | -92% | -84% | -1.01 | 126 |
| Price above moving average | ADA | n=50 | -56% | -65% | -83% | -88% | -0.33 | 66 |
| Price above moving average | ATOM | n=100 | -69% | -83% | -83% | -89% | -0.76 | 44 |
| Price above moving average | AVAX | n=20 | -85% | -77% | -91% | -89% | -1.12 | 116 |
| Price above moving average | BCH | n=200 | -77% | -49% | -81% | -71% | -1.11 | 46 |
| Price above moving average | BTC | n=200 | -20% | -5% | -37% | -53% | -0.14 | 30 |
| Price above moving average | DOGE | n=200 | -37% | -56% | -80% | -88% | -0.08 | 22 |
| Price above moving average | DOT | n=50 | -73% | -90% | -88% | -94% | -0.76 | 56 |
| Price above moving average | ETH | n=200 | -25% | -52% | -46% | -68% | -0.11 | 22 |
| Price above moving average | LINK | n=20 | -71% | -41% | -86% | -75% | -0.54 | 102 |
| Price above moving average | LTC | n=20 | -81% | -47% | -88% | -71% | -1.08 | 114 |
| Price above moving average | NEAR | n=50 | -28% | -46% | -79% | -88% | 0.16 | 46 |
| Price above moving average | SHIB | n=20 | -89% | -79% | -91% | -89% | -1.45 | 120 |
| Price above moving average | SOL | n=50 | -51% | -53% | -69% | -76% | -0.36 | 56 |
| Price above moving average | SUI | n=100 | +13% | -21% | -71% | -88% | 0.40 | 42 |
| Price above moving average | UNI | n=50 | +5% | -49% | -72% | -87% | 0.35 | 48 |
| Price above moving average | XLM | n=50 | -11% | +40% | -79% | -77% | 0.28 | 70 |
| Price above moving average | XRP | n=200 | +60% | +93% | -60% | -74% | 0.62 | 24 |
| RSI dip-buying | AAVE | low=20, high=75 | +93% | -2% | -15% | -84% | 1.14 | 2 |
| RSI dip-buying | ADA | low=25, high=55 | -6% | -65% | -35% | -88% | 0.08 | 7 |
| RSI dip-buying | ATOM | low=20, high=75 | +49% | -83% | -9% | -89% | 1.17 | 2 |
| RSI dip-buying | AVAX | low=30, high=65 | -39% | -77% | -70% | -89% | -0.06 | 13 |
| RSI dip-buying | BCH | low=25, high=65 | -27% | -49% | -50% | -71% | -0.30 | 3 |
| RSI dip-buying | BTC | low=20, high=75 | +6% | -5% | -29% | -53% | 0.22 | 3 |
| RSI dip-buying | DOGE | low=25, high=65 | -1% | -56% | -28% | -88% | 0.11 | 5 |
| RSI dip-buying | DOT | low=20, high=75 | +12% | -90% | -25% | -94% | 0.33 | 3 |
| RSI dip-buying | ETH | low=20, high=65 | +27% | -52% | -13% | -68% | 0.56 | 5 |
| RSI dip-buying | LINK | low=25, high=65 | +61% | -41% | -22% | -75% | 0.77 | 6 |
| RSI dip-buying | LTC | low=30, high=65 | -1% | -47% | -29% | -71% | 0.15 | 9 |
| RSI dip-buying | NEAR | low=35, high=75 | -4% | -46% | -79% | -88% | 0.39 | 9 |
| RSI dip-buying | SHIB | low=20, high=65 | +5% | -79% | -18% | -89% | 0.22 | 2 |
| RSI dip-buying | SOL | low=20, high=75 | -2% | -53% | -36% | -76% | 0.11 | 3 |
| RSI dip-buying | SUI | low=30, high=55 | -33% | -21% | -65% | -88% | -0.05 | 13 |
| RSI dip-buying | UNI | low=25, high=75 | +232% | -49% | -27% | -87% | 1.23 | 6 |
| RSI dip-buying | XLM | low=30, high=65 | +43% | +40% | -52% | -77% | 0.56 | 11 |
| RSI dip-buying | XRP | low=35, high=75 | -32% | +93% | -67% | -74% | 0.00 | 9 |
