# Kill-First Desk · paper trading

Updated 2026-10-31 17:29:07 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 518 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $71.06 | $68.71 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 5 |
| Closed trades | 8 | 7 |
| Win rate | 0% | 0% |
| Avg win | $0.00 | $0.00 |
| Avg loss | $-0.96 | $-0.99 |
| Expectancy per trade | $-0.957 | $-0.987 |
| Return per $ bet | -65.1% | -65.6% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 8 and 7).

Lab: 18,363 coins fully tracked for 4 hours, 5,280 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 26,095 · young coins waiting for a second look: 1,656

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 26,157 | 6,583 | 1 (0%) |
| No security report | 1,044 | 329 | 3 (1%) |
| Already pumped this hour | 47 | 9 | 1 (11%) |
| Liquidity too low | 42 | 7 | 0 (0%) |
| Fading: few trades in last 5 min | 40 | 12 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 31 | 10 | 0 (0%) |
| Council score too low | 31 | 6 | 0 (0%) |
| Top 10 holders own too much | 16 | 1 | 0 (0%) |
| No market yet | 8 | 0 | — |
| Dev wallet already selling | 7 | 2 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
