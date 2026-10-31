# Kill-First Desk · paper trading

Updated 2026-10-31 08:14:34 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 0 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.62 | $72.84 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 0 |
| Closed trades | 4 | 5 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.10 | $-0.83 |
| Expectancy per trade | $-1.095 | $-0.832 |
| Return per $ bet | -72.1% | -54.7% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 4 and 5).

Lab: 8,504 coins fully tracked for 4 hours, 4,474 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 13,077 · young coins waiting for a second look: 739

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 14,696 | 3,116 | 0 (0%) |
| No security report | 539 | 128 | 2 (2%) |
| Fading: few trades in last 5 min | 23 | 12 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 23 | 10 | 0 (0%) |
| Already pumped this hour | 18 | 7 | 1 (14%) |
| Liquidity too low | 14 | 4 | 0 (0%) |
| Council score too low | 12 | 3 | 0 (0%) |
| No market yet | 5 | 0 | — |
| Top 10 holders own too much | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 1 | 0 | — |
| Dev wallet already selling | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 01:07 | MONEKO | 82 | Hard stop | $-0.89 |
| 10-31 01:00 | REMARC | 76 | Hard stop | $-0.78 |
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- api.rugcheck.xyz (400): 273
- api.rugcheck.xyz (ConnectionError): 1
