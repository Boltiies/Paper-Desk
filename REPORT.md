# Kill-First Desk · paper trading

Updated 2026-11-01 10:08:28 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 410 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $60.06 | $59.43 |
| Started with | $77.00 | $77.00 |
| Open trades | 4 | 2 |
| Closed trades | 32 | 28 |
| Win rate | 9% | 7% |
| Avg win | $0.53 | $0.48 |
| Avg loss | $-0.80 | $-0.71 |
| Expectancy per trade | $-0.674 | $-0.628 |
| Return per $ bet | -51.1% | -46.0% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 32 and 28).

Lab: 39,582 coins fully tracked for 4 hours, 2,953 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 49,196 · young coins waiting for a second look: 625 · RugCheck rechecks: 21

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 49,687 | 13,015 | 5 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 196 | 64 | 0 (0%) |
| Already pumped this hour | 158 | 43 | 6 (14%) |
| Fading: few trades in last 5 min | 151 | 49 | 0 (0%) |
| Council score too low | 102 | 30 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 76 | 30 | 0 (0%) |
| Top 10 holders own too much | 66 | 24 | 0 (0%) |
| Dev holds too much | 18 | 6 | 0 (0%) |
| No market yet | 13 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 10:05 | SCRAT | 70 | Hard stop | $-0.49 |
| 11-01 08:08 | niketyson | 88 | Hard stop | $-0.70 |
| 11-01 06:17 | GLIPUP | 78 | Coin died: no buyers | $-0.17 |
| 11-01 06:07 | Solana | 87 | Hard stop | $-0.69 |
| 11-01 05:50 | GTA 6 Coin | 72 | Hard stop | $-0.48 |
| 11-01 04:27 | Movember | 77 | Hard stop | $-0.99 |
| 11-01 04:08 | NIGUIN | 72 | Hard stop | $-0.66 |
| 11-01 04:04 | YouTube | 90 | Trailing stop | $+0.39 |
| 11-01 03:52 | ELON | 78 | Hard stop | $-0.67 |
| 11-01 02:30 | Reaper | 79 | Hard stop | $-0.98 |
| 11-01 02:14 | PUTIN | 80 | Hard stop | $-0.72 |
| 11-01 01:54 | BLUE | 82 | Hard stop | $-0.86 |
| 11-01 01:02 | NNN | 84 | Hard stop | $-1.19 |
| 11-01 00:54 | CASHCAT | 98 | Hard stop | $-0.22 |
| 10-31 23:41 | INKKY | 87 | Hard stop | $-0.94 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 1
