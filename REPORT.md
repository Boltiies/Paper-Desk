# Kill-First Desk · paper trading

Updated 2026-10-31 18:05:40 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 833 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $70.54 | $67.75 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 4 |
| Closed trades | 10 | 9 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-0.89 | $-0.92 |
| Expectancy per trade | $-0.887 | $-0.919 |
| Return per $ bet | -61.1% | -61.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 10 and 9).

Lab: 19,094 coins fully tracked for 4 hours, 5,350 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 27,233 · young coins waiting for a second look: 1,844

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 27,079 | 6,816 | 1 (0%) |
| No security report | 1,044 | 329 | 3 (1%) |
| Already pumped this hour | 55 | 9 | 1 (11%) |
| Liquidity too low | 45 | 7 | 0 (0%) |
| Fading: few trades in last 5 min | 44 | 12 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 34 | 12 | 0 (0%) |
| Council score too low | 34 | 6 | 0 (0%) |
| Top 10 holders own too much | 19 | 7 | 0 (0%) |
| No market yet | 8 | 0 | — |
| Dev wallet already selling | 7 | 2 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Dev holds too much | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 18:01 | KIM | 83 | Hard stop | $-0.86 |
| 10-31 17:30 | GTA 6 Coin | 80 | Dev wallet sold, got out | $-0.34 |
| 10-31 16:45 | DOUGHBRIKS | 70 | Hard stop | $-0.72 |
| 10-31 16:22 | MAX | 71 | Hard stop | $-0.05 |
| 10-31 16:19 | GTA 6 Coin | 72 | Dev wallet sold, got out | $-1.55 |
| 10-31 15:50 | billy | 72 | Hard stop | $-0.96 |
| 10-31 01:07 | MONEKO | 82 | Hard stop | $-0.89 |
| 10-31 01:00 | REMARC | 76 | Hard stop | $-0.78 |
| 10-30 23:56 | PUMPCAT | 86 | Dev wallet sold, got out | $-1.62 |
| 10-30 23:25 | iCat | 83 | Hard stop | $-1.08 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 5
- api.rugcheck.xyz (ConnectionError): 4
