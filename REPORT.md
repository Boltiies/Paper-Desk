# Kill-First Desk · paper trading

Updated 2026-11-01 17:25:16 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,505 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $50.95 | $56.70 |
| Started with | $77.00 | $77.00 |
| Open trades | 5 | 3 |
| Closed trades | 51 | 40 |
| Win rate | 16% | 12% |
| Avg win | $0.80 | $0.87 |
| Avg loss | $-0.76 | $-0.69 |
| Expectancy per trade | $-0.511 | $-0.495 |
| Return per $ bet | -41.4% | -37.8% |

## Does the council have an edge?

Council picks return -41.4% per dollar bet, random picks -37.8%. Gap: **-3.6 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 46,265 coins fully tracked for 4 hours, 5,575 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 61,097 · young coins waiting for a second look: 2,520 · RugCheck rechecks: 39

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 59,379 | 15,755 | 7 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 284 | 81 | 0 (0%) |
| Already pumped this hour | 211 | 50 | 6 (12%) |
| Fading: few trades in last 5 min | 167 | 54 | 0 (0%) |
| Council score too low | 146 | 39 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 103 | 39 | 0 (0%) |
| Top 10 holders own too much | 99 | 32 | 0 (0%) |
| Dev holds too much | 24 | 8 | 0 (0%) |
| Dev wallet already selling | 20 | 7 | 0 (0%) |
| Too many open trades | 17 | 2 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 17:09 | GOON | 80 | Hard stop | $-0.91 |
| 11-01 16:30 | RS2s | 80 | Coin died: no buyers | $-0.54 |
| 11-01 15:50 | pairless | 80 | Trailing stop | $+0.65 |
| 11-01 14:57 | Numbat | 71 | Hard stop | $-0.52 |
| 11-01 14:54 | DOGE | 72 | Hard stop | $-0.56 |
| 11-01 14:48 | Alexander | 78 | Hard stop | $-0.77 |
| 11-01 14:29 | REGRETAMINE | 72 | Coin died: no buyers | $-0.40 |
| 11-01 14:07 | Ghost | 72 | Hard stop | $-0.57 |
| 11-01 14:00 | Texocoin | 71 | Hard stop | $-0.64 |
| 11-01 13:55 | BAMF | 76 | Hard stop | $-0.71 |
| 11-01 13:31 | REGRETAMINE | 72 | Trailing stop | $+0.99 |
| 11-01 13:05 | REGRETAMINE | 72 | Hard stop | $-0.70 |
| 11-01 12:49 | MARS | 75 | Trailing stop | $+0.19 |
| 11-01 12:29 | MARS | 80 | Hard stop | $-0.96 |
| 11-01 12:15 | UPVEMBER | 79 | Hard stop | $-0.92 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 12
