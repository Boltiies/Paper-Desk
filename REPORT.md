# Kill-First Desk · paper trading

Updated 2026-11-02 03:19:20 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 898 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $50.31 | $52.49 |
| Started with | $77.00 | $77.00 |
| Open trades | 4 | 4 |
| Closed trades | 62 | 55 |
| Win rate | 15% | 15% |
| Avg win | $0.76 | $0.68 |
| Avg loss | $-0.73 | $-0.67 |
| Expectancy per trade | $-0.516 | $-0.473 |
| Return per $ bet | -42.9% | -37.6% |

## Does the council have an edge?

Council picks return -42.9% per dollar bet, random picks -37.6%. Gap: **-5.4 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 61,447 coins fully tracked for 4 hours, 5,963 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 80,834 · young coins waiting for a second look: 2,819 · RugCheck rechecks: 50

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 78,357 | 19,564 | 12 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 399 | 123 | 0 (0%) |
| Fading: few trades in last 5 min | 314 | 113 | 0 (0%) |
| Already pumped this hour | 263 | 74 | 7 (9%) |
| Council score too low | 192 | 60 | 2 (3%) |
| Danger flag: Creator history of rugged tokens | 127 | 49 | 0 (0%) |
| Top 10 holders own too much | 121 | 41 | 1 (2%) |
| No market yet | 42 | 0 | — |
| Dev holds too much | 29 | 8 | 0 (0%) |
| Dev wallet already selling | 25 | 8 | 0 (0%) |
| Too many open trades | 18 | 3 | 1 (33%) |
| Sell test failed (honeypot or no route) | 9 | 3 | 0 (0%) |
| Liquidity not locked or burned | 2 | 2 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 03:14 | TrumpWars | 73 | Hard stop | $-0.62 |
| 11-02 02:04 | F7931A | 73 | Hard stop | $-0.48 |
| 11-02 01:16 | Heidou | 78 | Hard stop | $-1.03 |
| 11-02 00:15 | STEALTH | 76 | Dev wallet sold, got out | $-0.24 |
| 11-02 00:04 | LEARJET | 70 | Trailing stop | $+0.41 |
| 11-01 23:50 | Grok | 90 | Trailing stop | $-0.56 |
| 11-01 22:35 | Amazon | 79 | Dev wallet sold, got out | $-1.12 |
| 11-01 20:19 | CHOO | 85 | Hard stop | $-0.12 |
| 11-01 17:36 | Leverhedge | 82 | Hard stop | $-0.85 |
| 11-01 17:32 | VETO | 74 | Hard stop | $-0.53 |
| 11-01 17:27 | Sperm | 73 | Hard stop | $-0.76 |
| 11-01 17:09 | GOON | 80 | Hard stop | $-0.91 |
| 11-01 16:30 | RS2s | 80 | Coin died: no buyers | $-0.54 |
| 11-01 15:50 | pairless | 80 | Trailing stop | $+0.65 |
| 11-01 14:57 | Numbat | 71 | Hard stop | $-0.52 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- lite-api.jup.ag (400): 1
