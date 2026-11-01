# Kill-First Desk · paper trading

Updated 2026-11-01 17:35:44 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,570 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $50.42 | $56.43 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 3 |
| Closed trades | 53 | 40 |
| Win rate | 15% | 12% |
| Avg win | $0.80 | $0.87 |
| Avg loss | $-0.75 | $-0.69 |
| Expectancy per trade | $-0.516 | $-0.495 |
| Return per $ bet | -42.1% | -37.8% |

## Does the council have an edge?

Council picks return -42.1% per dollar bet, random picks -37.8%. Gap: **-4.2 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 46,489 coins fully tracked for 4 hours, 5,613 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 61,450 · young coins waiting for a second look: 2,605 · RugCheck rechecks: 39

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 59,639 | 15,781 | 7 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 288 | 81 | 0 (0%) |
| Already pumped this hour | 212 | 50 | 6 (12%) |
| Fading: few trades in last 5 min | 168 | 54 | 0 (0%) |
| Council score too low | 147 | 40 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 103 | 39 | 0 (0%) |
| Top 10 holders own too much | 100 | 32 | 0 (0%) |
| Dev holds too much | 24 | 8 | 0 (0%) |
| Dev wallet already selling | 20 | 7 | 0 (0%) |
| Too many open trades | 17 | 2 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 13:55 | BAMF | 76 | Hard stop | $-0.71 |
| 11-01 13:31 | REGRETAMINE | 72 | Trailing stop | $+0.99 |
| 11-01 13:05 | REGRETAMINE | 72 | Hard stop | $-0.70 |
| 11-01 12:49 | MARS | 75 | Trailing stop | $+0.19 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 12
