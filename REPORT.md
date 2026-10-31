# Kill-First Desk · paper trading

Updated 2026-10-31 00:07:56 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 89 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $73.88 | $74.96 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 1 |
| Closed trades | 2 | 2 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.35 | $-0.81 |
| Expectancy per trade | $-1.353 | $-0.815 |
| Return per $ bet | -88.4% | -53.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 2 and 2).

Lab: 0 coins fully tracked for 4 hours, 2,975 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 1,939 · young coins waiting for a second look: 2,999

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 1,896 | 159 | 0 (0%) |
| Fading: few trades in last 5 min | 13 | 3 | 0 (0%) |
| Liquidity too low | 9 | 1 | 0 (0%) |
| Already pumped this hour | 7 | 0 | — |
| Council score too low | 6 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 4 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 1 | 0 | — |
| Top 10 holders own too much | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
