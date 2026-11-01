# Kill-First Desk · paper trading

Updated 2026-11-01 15:38:44 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 574 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $54.27 | $56.82 |
| Started with | $77.00 | $77.00 |
| Open trades | 5 | 5 |
| Closed trades | 48 | 38 |
| Win rate | 15% | 13% |
| Avg win | $0.83 | $0.87 |
| Avg loss | $-0.76 | $-0.71 |
| Expectancy per trade | $-0.527 | $-0.502 |
| Return per $ bet | -42.3% | -38.2% |

## Does the council have an edge?

Council picks return -42.3% per dollar bet, random picks -38.2%. Gap: **-4.1 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 43,996 coins fully tracked for 4 hours, 5,297 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 57,311 · young coins waiting for a second look: 1,533 · RugCheck rechecks: 33

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 56,657 | 15,027 | 7 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 261 | 76 | 0 (0%) |
| Already pumped this hour | 200 | 49 | 6 (12%) |
| Fading: few trades in last 5 min | 157 | 51 | 0 (0%) |
| Council score too low | 137 | 34 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 94 | 35 | 0 (0%) |
| Top 10 holders own too much | 92 | 31 | 0 (0%) |
| Dev holds too much | 24 | 7 | 0 (0%) |
| Dev wallet already selling | 18 | 6 | 0 (0%) |
| Too many open trades | 15 | 0 | — |
| No market yet | 13 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 12:00 | SA | 70 | Hard stop | $-0.54 |
| 11-01 11:42 | BLACKED | 80 | Trailing stop | $+2.50 |
| 11-01 11:13 | MARVIN | 73 | Trailing stop | $+0.53 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 6
