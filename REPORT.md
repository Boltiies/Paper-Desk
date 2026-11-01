# Kill-First Desk · paper trading

Updated 2026-11-01 18:48:44 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,893 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $49.96 | $56.87 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 3 |
| Closed trades | 54 | 41 |
| Win rate | 15% | 12% |
| Avg win | $0.80 | $0.87 |
| Avg loss | $-0.75 | $-0.69 |
| Expectancy per trade | $-0.523 | $-0.504 |
| Return per $ bet | -42.4% | -38.4% |

## Does the council have an edge?

Council picks return -42.4% per dollar bet, random picks -38.4%. Gap: **-4.0 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 48,082 coins fully tracked for 4 hours, 5,812 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 63,753 · young coins waiting for a second look: 2,986 · RugCheck rechecks: 41

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 61,504 | 16,253 | 7 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 297 | 85 | 0 (0%) |
| Already pumped this hour | 217 | 51 | 6 (12%) |
| Fading: few trades in last 5 min | 194 | 55 | 0 (0%) |
| Council score too low | 151 | 41 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 109 | 40 | 0 (0%) |
| Top 10 holders own too much | 105 | 33 | 0 (0%) |
| Dev holds too much | 25 | 8 | 0 (0%) |
| Dev wallet already selling | 20 | 7 | 0 (0%) |
| Too many open trades | 17 | 2 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 13:55 | BAMF | 76 | Hard stop | $-0.71 |
| 11-01 13:31 | REGRETAMINE | 72 | Trailing stop | $+0.99 |
| 11-01 13:05 | REGRETAMINE | 72 | Hard stop | $-0.70 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 14
