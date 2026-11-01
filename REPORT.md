# Kill-First Desk · paper trading

Updated 2026-11-01 23:54:32 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,315 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $50.81 | $56.50 |
| Started with | $77.00 | $77.00 |
| Open trades | 4 | 2 |
| Closed trades | 57 | 51 |
| Win rate | 14% | 16% |
| Avg win | $0.80 | $0.68 |
| Avg loss | $-0.74 | $-0.67 |
| Expectancy per trade | $-0.527 | $-0.454 |
| Return per $ bet | -43.2% | -35.6% |

## Does the council have an edge?

Council picks return -43.2% per dollar bet, random picks -35.6%. Gap: **-7.6 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 55,674 coins fully tracked for 4 hours, 6,748 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 75,144 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 49

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 72,633 | 18,198 | 11 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 358 | 105 | 0 (0%) |
| Fading: few trades in last 5 min | 268 | 89 | 0 (0%) |
| Already pumped this hour | 251 | 66 | 6 (9%) |
| Council score too low | 176 | 52 | 2 (4%) |
| Danger flag: Creator history of rugged tokens | 119 | 46 | 0 (0%) |
| Top 10 holders own too much | 113 | 37 | 0 (0%) |
| No market yet | 40 | 0 | — |
| Dev holds too much | 27 | 8 | 0 (0%) |
| Dev wallet already selling | 23 | 8 | 0 (0%) |
| Too many open trades | 17 | 2 | 0 (0%) |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 2 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 14:54 | DOGE | 72 | Hard stop | $-0.56 |
| 11-01 14:48 | Alexander | 78 | Hard stop | $-0.77 |
| 11-01 14:29 | REGRETAMINE | 72 | Coin died: no buyers | $-0.40 |
| 11-01 14:07 | Ghost | 72 | Hard stop | $-0.57 |
| 11-01 14:00 | Texocoin | 71 | Hard stop | $-0.64 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
