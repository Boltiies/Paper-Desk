# Kill-First Desk · paper trading

Updated 2026-10-31 19:19:07 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,462 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.08 | $67.13 |
| Started with | $77.00 | $77.00 |
| Open trades | 4 | 5 |
| Closed trades | 13 | 10 |
| Win rate | 8% | 0% |
| Avg win | $1.16 | $0.00 |
| Avg loss | $-0.89 | $-0.91 |
| Expectancy per trade | $-0.736 | $-0.910 |
| Return per $ bet | -51.3% | -61.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 13 and 10).

Lab: 20,711 coins fully tracked for 4 hours, 5,382 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 29,927 · young coins waiting for a second look: 2,561

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 28,993 | 7,235 | 1 (0%) |
| No security report | 1,047 | 329 | 3 (1%) |
| Already pumped this hour | 70 | 10 | 1 (10%) |
| Liquidity too low | 61 | 10 | 0 (0%) |
| Fading: few trades in last 5 min | 53 | 14 | 0 (0%) |
| Council score too low | 44 | 6 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 39 | 14 | 0 (0%) |
| Top 10 holders own too much | 20 | 7 | 0 (0%) |
| No market yet | 8 | 0 | — |
| Dev wallet already selling | 7 | 3 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Dev holds too much | 2 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 19:01 | Satoshi | 91 | Hard stop | $-0.89 |
| 10-31 18:47 | Puffen | 73 | Hard stop | $-0.98 |
| 10-31 18:18 | HUSS | 72 | Trailing stop | $+1.16 |
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
- api.rugcheck.xyz (ConnectionError): 7
