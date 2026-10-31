# Kill-First Desk · paper trading

Updated 2026-10-31 00:51:22 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 103 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $73.54 | $74.62 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 2 |
| Closed trades | 2 | 2 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.35 | $-0.81 |
| Expectancy per trade | $-1.353 | $-0.815 |
| Return per $ bet | -88.4% | -53.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 2 and 2).

Lab: 0 coins fully tracked for 4 hours, 4,008 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 3,121 · young coins waiting for a second look: 2,955

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 3,092 | 388 | 0 (0%) |
| Fading: few trades in last 5 min | 19 | 7 | 0 (0%) |
| Already pumped this hour | 14 | 0 | — |
| Liquidity too low | 13 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 9 | 1 | 0 (0%) |
| Council score too low | 9 | 2 | 0 (0%) |
| Top 10 holders own too much | 2 | 0 | — |
| No market yet | 2 | 0 | — |
| Sell test failed (honeypot or no route) | 1 | 0 | — |
| Dev wallet already selling | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
