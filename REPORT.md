# Kill-First Desk · paper trading

Updated 2026-10-31 16:03:47 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 43 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $71.66 | $72.84 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 0 |
| Closed trades | 5 | 5 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.07 | $-0.83 |
| Expectancy per trade | $-1.069 | $-0.832 |
| Return per $ bet | -71.0% | -54.7% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 5 and 5).

Lab: 16,772 coins fully tracked for 4 hours, 4,963 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 23,718 · young coins waiting for a second look: 1,625

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 23,919 | 6,057 | 1 (0%) |
| No security report | 1,040 | 305 | 3 (1%) |
| Already pumped this hour | 28 | 7 | 1 (14%) |
| Fading: few trades in last 5 min | 25 | 12 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 24 | 10 | 0 (0%) |
| Liquidity too low | 21 | 4 | 0 (0%) |
| Council score too low | 17 | 3 | 0 (0%) |
| No market yet | 8 | 0 | — |
| Top 10 holders own too much | 3 | 1 | 0 (0%) |
| Dev wallet already selling | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 15:50 | billy | 72 | Hard stop | $-0.96 |
| 10-31 01:07 | MONEKO | 82 | Hard stop | $-0.89 |
| 10-31 01:00 | REMARC | 76 | Hard stop | $-0.78 |
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- api.rugcheck.xyz (400): 410
- api.rugcheck.xyz (ConnectionError): 5
