# What the lab learned

16,946 coins with a live market were followed for 4 hours, bought or not. "Ran" means it hit 2x at some point; "died" means trading had stopped by 4 hours. Base rate first, then each feature. Groups under ~50 coins are noise.

### Overall

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| All coins | 16946 | 1% | 99% | 0.00x |
| dropped before security | 16093 | 1% | 100% | 0.00x |
| failed security | 813 | 9% | 86% | 0.00x |
| passed security | 40 | 12% | 50% | 0.05x |

### By what the desk decided

If a kill reason's coins ran as often as the coins it bought, that filter isn't helping.

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| Dropped before security (low volume) | 16093 | 1% | 100% | 0.00x |
| No security report | 755 | 10% | 86% | 0.00x |
| Fading: few trades in last 5 min | 23 | 9% | 74% | 0.00x |
| Danger flag: Creator history of rugged tokens | 23 | 0% | 100% | 0.00x |
| Already pumped this hour | 18 | 17% | 33% | 0.08x |
| Liquidity too low | 14 | 0% | 100% | 0.00x |
| Council score too low | 12 | 8% | 17% | 0.52x |
| bought | 4 | 25% | 25% | 0.43x |
| Top 10 holders own too much | 2 | 0% | 50% | 0.03x |
| Dev wallet already selling | 1 | 100% | 0% | 0.24x |
| Sell test failed (honeypot or no route) | 1 | 0% | 100% | 0.00x |

## Coins that passed security

40 coins. These are the ones the council has to choose between.

### Council score

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| under 50 | 26 | 8% | 69% | 0.00x |
| 50 to 60 | 3 | 0% | 0% | 0.68x |
| 60 to 70 | 6 | 17% | 17% | 0.46x |
| 70 to 80 | 2 | 50% | 0% | 0.51x |
| 80+ | 3 | 33% | 33% | 0.10x |

### Trades in the last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 5 | 20 | 10% | 80% | 0.00x |
| 5 to 15 | 3 | 33% | 0% | 0.87x |
| 15 to 40 | 4 | 0% | 75% | 0.00x |
| 40 to 100 | 5 | 20% | 0% | 0.60x |
| 100+ | 8 | 12% | 12% | 0.48x |

### Buy share, last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.00 to 0.45 | 13 | 8% | 77% | 0.00x |
| 0.45 to 0.55 | 5 | 0% | 40% | 0.44x |
| 0.55 to 0.65 | 7 | 14% | 14% | 0.28x |
| 0.65 to 0.75 | 4 | 25% | 0% | 0.68x |
| 0.75 to 1.01 | 3 | 33% | 67% | 0.00x |
| unknown | 8 | 12% | 62% | 0.00x |

### Speeding up (last 5 min vs hourly pace)

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.0 to 0.5 | 31 | 10% | 61% | 0.00x |
| 0.5 to 1.0 | 5 | 0% | 20% | 0.32x |
| 1.0 to 1.5 | 1 | 0% | 0% | 0.77x |
| 1.5 to 3.0 | 2 | 50% | 0% | 2.81x |
| 3.0+ | 1 | 100% | 0% | 0.24x |

### Price change, last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| -1000000000% to -10% | 7 | 14% | 43% | 0.28x |
| -10% to 0% | 6 | 0% | 67% | 0.00x |
| 0% to 10% | 10 | 10% | 60% | 0.00x |
| 10% to 30% | 5 | 20% | 0% | 0.32x |
| 30%+ | 3 | 33% | 33% | 0.60x |
| unknown | 9 | 11% | 67% | 0.00x |

### Price change, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| -1000000000% to 0% | 21 | 5% | 67% | 0.00x |
| 0% to 50% | 10 | 20% | 40% | 0.19x |
| 50% to 100% | 6 | 33% | 17% | 0.38x |
| 100% to 200% | 3 | 0% | 33% | 0.77x |

### Buy share, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.00 to 0.50 | 7 | 0% | 43% | 0.44x |
| 0.50 to 0.60 | 28 | 14% | 54% | 0.00x |
| 0.60 to 0.70 | 3 | 0% | 33% | 0.28x |
| 0.70 to 1.01 | 2 | 50% | 50% | 0.12x |

### Volume, 24 hours

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $40,000 | 2 | 50% | 50% | 0.12x |
| $40,000 to $100,000 | 23 | 13% | 70% | 0.00x |
| $100,000 to $300,000 | 9 | 11% | 22% | 0.44x |
| $300,000 to $1,000,000 | 5 | 0% | 20% | 0.77x |
| $1,000,000+ | 1 | 0% | 0% | 1.67x |

### Liquidity

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $5,000 | 27 | 15% | 70% | 0.00x |
| $5,000 to $20,000 | 6 | 0% | 0% | 0.50x |
| $20,000 to $50,000 | 4 | 25% | 25% | 0.55x |
| $50,000+ | 3 | 0% | 0% | 1.04x |

### Market cap

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $30,000 | 30 | 13% | 63% | 0.00x |
| $30,000 to $100,000 | 6 | 17% | 17% | 0.45x |
| $100,000 to $300,000 | 1 | 0% | 0% | 1.00x |
| $1,000,000+ | 3 | 0% | 0% | 1.04x |

### Coin age

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 min to 15 min | 1 | 100% | 0% | 0.24x |
| 15 min to 60 min | 33 | 12% | 58% | 0.00x |
| 60 min to 240 min | 2 | 0% | 50% | 0.38x |
| 1440 min+ | 4 | 0% | 0% | 1.03x |

### Holders

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 100 | 2 | 0% | 100% | 0.00x |
| 100 to 300 | 15 | 13% | 80% | 0.00x |
| 300 to 1000 | 10 | 10% | 50% | 0.16x |
| 1000 to 3000 | 9 | 22% | 0% | 0.68x |
| 3000+ | 4 | 0% | 25% | 1.03x |

### New holders per minute

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 1 | 40 | 12% | 50% | 0.05x |

### Average trade size, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $20 | 1 | 0% | 0% | 1.01x |
| $20 to $50 | 25 | 4% | 56% | 0.00x |
| $50 to $150 | 12 | 25% | 50% | 0.16x |
| $150 to $500 | 1 | 0% | 0% | 1.67x |
| $500+ | 1 | 100% | 0% | 0.24x |

### Social links

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 1 | 1 | 0% | 100% | 0.00x |
| 1 to 2 | 12 | 25% | 42% | 0.26x |
| 2 to 3 | 21 | 10% | 57% | 0.00x |
| 3 to 99 | 6 | 0% | 33% | 0.29x |

