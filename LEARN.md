# What the lab learned

26,006 coins with a live market were followed for 4 hours, bought or not. "Ran" means it hit 2x at some point; "died" means trading had stopped by 4 hours. Base rate first, then each feature. Groups under ~50 coins are noise.

### Overall

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| All coins | 26006 | 2% | 99% | 0.00x |
| dropped before security | 24627 | 1% | 100% | 0.00x |
| failed security | 1252 | 12% | 85% | 0.00x |
| passed security | 127 | 13% | 64% | 0.00x |

### By what the desk decided

If a kill reason's coins ran as often as the coins it bought, that filter isn't helping.

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| Dropped before security (low volume) | 24627 | 1% | 100% | 0.00x |
| No security report | 1049 | 11% | 87% | 0.00x |
| Already pumped this hour | 71 | 34% | 48% | 0.01x |
| Liquidity too low | 63 | 14% | 97% | 0.00x |
| Fading: few trades in last 5 min | 55 | 7% | 82% | 0.00x |
| Council score too low | 46 | 9% | 54% | 0.00x |
| Danger flag: Creator history of rugged tokens | 40 | 0% | 95% | 0.00x |
| Top 10 holders own too much | 23 | 17% | 65% | 0.00x |
| bought | 17 | 35% | 24% | 0.10x |
| Dev wallet already selling | 8 | 38% | 75% | 0.00x |
| Sell test failed (honeypot or no route) | 4 | 0% | 75% | 0.00x |
| Dev holds too much | 2 | 50% | 0% | 0.81x |
| passed | 1 | 0% | 100% | 0.00x |

## Coins that passed security

127 coins. These are the ones the council has to choose between.

### Council score

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| under 50 | 76 | 5% | 78% | 0.00x |
| 50 to 60 | 10 | 10% | 30% | 0.48x |
| 60 to 70 | 17 | 18% | 53% | 0.00x |
| 70 to 80 | 13 | 23% | 54% | 0.00x |
| 80+ | 11 | 55% | 27% | 0.10x |

### Trades in the last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 5 | 30 | 7% | 87% | 0.00x |
| 5 to 15 | 21 | 19% | 62% | 0.00x |
| 15 to 40 | 17 | 6% | 82% | 0.00x |
| 40 to 100 | 19 | 16% | 47% | 0.19x |
| 100+ | 40 | 18% | 48% | 0.04x |

### Buy share, last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.00 to 0.45 | 49 | 4% | 80% | 0.00x |
| 0.45 to 0.55 | 21 | 5% | 57% | 0.00x |
| 0.55 to 0.65 | 24 | 21% | 33% | 0.16x |
| 0.65 to 0.75 | 11 | 45% | 45% | 0.32x |
| 0.75 to 1.01 | 12 | 25% | 83% | 0.00x |
| unknown | 10 | 10% | 70% | 0.00x |

### Speeding up (last 5 min vs hourly pace)

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.0 to 0.5 | 65 | 5% | 75% | 0.00x |
| 0.5 to 1.0 | 16 | 6% | 25% | 0.62x |
| 1.0 to 1.5 | 7 | 0% | 57% | 0.00x |
| 1.5 to 3.0 | 9 | 22% | 33% | 0.10x |
| 3.0+ | 30 | 37% | 70% | 0.00x |

### Price change, last 5 minutes

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| -1000000000% to -10% | 34 | 12% | 68% | 0.00x |
| -10% to 0% | 34 | 3% | 68% | 0.00x |
| 0% to 10% | 16 | 12% | 62% | 0.00x |
| 10% to 30% | 13 | 15% | 23% | 0.24x |
| 30%+ | 19 | 37% | 74% | 0.00x |
| unknown | 11 | 9% | 73% | 0.00x |

### Price change, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| -1000000000% to 0% | 61 | 2% | 75% | 0.00x |
| 0% to 50% | 28 | 25% | 46% | 0.06x |
| 50% to 100% | 15 | 20% | 60% | 0.00x |
| 100% to 200% | 17 | 18% | 65% | 0.00x |
| 200%+ | 6 | 50% | 33% | 0.18x |

### Buy share, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0.00 to 0.50 | 16 | 6% | 56% | 0.00x |
| 0.50 to 0.60 | 81 | 9% | 68% | 0.00x |
| 0.60 to 0.70 | 21 | 29% | 43% | 0.17x |
| 0.70 to 1.01 | 9 | 33% | 89% | 0.00x |

### Volume, 24 hours

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $40,000 | 25 | 36% | 68% | 0.00x |
| $40,000 to $100,000 | 65 | 8% | 78% | 0.00x |
| $100,000 to $300,000 | 26 | 12% | 46% | 0.05x |
| $300,000 to $1,000,000 | 6 | 0% | 17% | 0.89x |
| $1,000,000+ | 5 | 0% | 0% | 1.07x |

### Liquidity

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $5,000 | 88 | 14% | 78% | 0.00x |
| $5,000 to $20,000 | 19 | 16% | 42% | 0.07x |
| $20,000 to $50,000 | 12 | 17% | 33% | 0.09x |
| $50,000+ | 8 | 0% | 0% | 1.06x |

### Market cap

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $30,000 | 96 | 11% | 75% | 0.00x |
| $30,000 to $100,000 | 21 | 29% | 43% | 0.04x |
| $100,000 to $300,000 | 2 | 0% | 0% | 0.88x |
| $300,000 to $1,000,000 | 2 | 0% | 0% | 1.09x |
| $1,000,000+ | 6 | 0% | 0% | 1.04x |

### Coin age

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 min to 15 min | 39 | 23% | 74% | 0.00x |
| 15 min to 60 min | 74 | 9% | 69% | 0.00x |
| 60 min to 240 min | 3 | 0% | 33% | 0.49x |
| 240 min to 1440 min | 3 | 0% | 0% | 1.07x |
| 1440 min+ | 8 | 12% | 0% | 1.02x |

### Holders

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 100 | 8 | 12% | 100% | 0.00x |
| 100 to 300 | 42 | 14% | 79% | 0.00x |
| 300 to 1000 | 43 | 7% | 72% | 0.00x |
| 1000 to 3000 | 23 | 26% | 30% | 0.14x |
| 3000+ | 11 | 9% | 18% | 1.04x |

### New holders per minute

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 1 | 127 | 13% | 64% | 0.00x |

### Average trade size, last hour

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| $0 to $20 | 5 | 40% | 60% | 0.00x |
| $20 to $50 | 88 | 7% | 68% | 0.00x |
| $50 to $150 | 24 | 21% | 58% | 0.00x |
| $150 to $500 | 6 | 33% | 33% | 1.01x |
| $500+ | 4 | 50% | 50% | 0.12x |

### Social links

| Group | Coins | Ran 2x+ | Died | Median after 4h |
|---|---|---|---|---|
| 0 to 1 | 5 | 20% | 80% | 0.00x |
| 1 to 2 | 32 | 12% | 66% | 0.00x |
| 2 to 3 | 75 | 13% | 68% | 0.00x |
| 3 to 99 | 15 | 13% | 33% | 0.14x |

