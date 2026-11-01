# Kill-First Desk · paper trading

Updated 2026-11-01 13:23:57 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 2,425 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $56.97 | $59.73 |
| Started with | $77.00 | $77.00 |
| Open trades | 5 | 5 |
| Closed trades | 40 | 34 |
| Win rate | 15% | 12% |
| Avg win | $0.80 | $0.78 |
| Avg loss | $-0.79 | $-0.73 |
| Expectancy per trade | $-0.553 | $-0.555 |
| Return per $ bet | -43.2% | -41.7% |

## Does the council have an edge?

Council picks return -43.2% per dollar bet, random picks -41.7%. Gap: **-1.6 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 41,971 coins fully tracked for 4 hours, 4,272 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 53,336 · young coins waiting for a second look: 1,071 · RugCheck rechecks: 25

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 53,266 | 14,193 | 5 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 226 | 72 | 0 (0%) |
| Already pumped this hour | 182 | 48 | 6 (12%) |
| Fading: few trades in last 5 min | 155 | 51 | 0 (0%) |
| Council score too low | 116 | 32 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 88 | 33 | 0 (0%) |
| Top 10 holders own too much | 83 | 26 | 0 (0%) |
| Dev holds too much | 19 | 6 | 0 (0%) |
| Dev wallet already selling | 14 | 6 | 0 (0%) |
| No market yet | 13 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |
| Too many open trades | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 11-01 06:17 | GLIPUP | 78 | Coin died: no buyers | $-0.17 |
| 11-01 06:07 | Solana | 87 | Hard stop | $-0.69 |
| 11-01 05:50 | GTA 6 Coin | 72 | Hard stop | $-0.48 |
| 11-01 04:27 | Movember | 77 | Hard stop | $-0.99 |
| 11-01 04:08 | NIGUIN | 72 | Hard stop | $-0.66 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 5
