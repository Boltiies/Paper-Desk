# Kill-First Desk · paper trading

Updated 2026-11-01 14:38:58 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 3,187 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $53.98 | $58.23 |
| Started with | $77.00 | $77.00 |
| Open trades | 5 | 3 |
| Closed trades | 45 | 37 |
| Win rate | 16% | 14% |
| Avg win | $0.83 | $0.87 |
| Avg loss | $-0.77 | $-0.71 |
| Expectancy per trade | $-0.521 | $-0.499 |
| Return per $ bet | -41.4% | -37.8% |

## Does the council have an edge?

Council picks return -41.4% per dollar bet, random picks -37.8%. Gap: **-3.5 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 42,992 coins fully tracked for 4 hours, 4,867 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 55,438 · young coins waiting for a second look: 1,258 · RugCheck rechecks: 27

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 55,118 | 14,643 | 6 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 241 | 75 | 0 (0%) |
| Already pumped this hour | 192 | 49 | 6 (12%) |
| Fading: few trades in last 5 min | 156 | 51 | 0 (0%) |
| Council score too low | 125 | 32 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 92 | 34 | 0 (0%) |
| Top 10 holders own too much | 89 | 31 | 0 (0%) |
| Dev holds too much | 22 | 6 | 0 (0%) |
| Dev wallet already selling | 16 | 6 | 0 (0%) |
| No market yet | 13 | 0 | — |
| Too many open trades | 9 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 10:37 | NOGE | 70 | Hard stop | $-0.65 |
| 11-01 10:05 | SCRAT | 70 | Hard stop | $-0.49 |
| 11-01 08:08 | niketyson | 88 | Hard stop | $-0.70 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 7
