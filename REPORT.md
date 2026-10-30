# Kill-First Desk · paper trading

Updated 2026-10-30 23:46:52 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 79 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $75.25 | $75.26 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 1 |
| Closed trades | 1 | 2 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.08 | $-0.81 |
| Expectancy per trade | $-1.082 | $-0.815 |
| Return per $ bet | -70.3% | -53.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 1 and 2).

Lab: 0 coins fully tracked for 4 hours, 2,453 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 1,369 · young coins waiting for a second look: 3,000

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 1,336 | 0 | — |
| Fading: few trades in last 5 min | 12 | 0 | — |
| Liquidity too low | 7 | 0 | — |
| Council score too low | 6 | 0 | — |
| Already pumped this hour | 3 | 0 | — |
| Danger flag: Creator history of rugged tokens | 1 | 0 | — |
| Sell test failed (honeypot or no route) | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
