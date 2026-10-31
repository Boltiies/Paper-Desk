# Kill-First Desk · paper trading

Updated 2026-10-31 01:02:22 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 187 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $73.41 | $74.15 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 2 |
| Closed trades | 3 | 3 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-1.16 | $-0.80 |
| Expectancy per trade | $-1.163 | $-0.804 |
| Return per $ bet | -75.8% | -52.4% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 3 and 3).

Lab: 0 coins fully tracked for 4 hours, 4,279 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 3,403 · young coins waiting for a second look: 2,982

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 3,337 | 388 | 0 (0%) |
| Fading: few trades in last 5 min | 20 | 7 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 14 | 1 | 0 (0%) |
| Liquidity too low | 14 | 2 | 0 (0%) |
| Already pumped this hour | 14 | 0 | — |
| Council score too low | 12 | 2 | 0 (0%) |
| Top 10 holders own too much | 2 | 0 | — |
| No market yet | 2 | 0 | — |
| Sell test failed (honeypot or no route) | 1 | 0 | — |
| Dev wallet already selling | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 01:00 | REMARC | 76 | Hard stop | $-0.78 |
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 2
