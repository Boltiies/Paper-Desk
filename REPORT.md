# Kill-First Desk · paper trading

Updated 2026-10-31 20:12:07 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,807 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.12 | $65.93 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 3 |
| Closed trades | 15 | 14 |
| Win rate | 13% | 0% |
| Avg win | $0.60 | $0.00 |
| Avg loss | $-0.88 | $-0.79 |
| Expectancy per trade | $-0.687 | $-0.789 |
| Return per $ bet | -48.0% | -54.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 15 and 14).

Lab: 21,935 coins fully tracked for 4 hours, 5,399 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 32,016 · young coins waiting for a second look: 3,000

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 30,612 | 7,592 | 2 (0%) |
| No security report | 1,049 | 329 | 3 (1%) |
| Already pumped this hour | 73 | 13 | 3 (23%) |
| Liquidity too low | 68 | 15 | 0 (0%) |
| Fading: few trades in last 5 min | 61 | 15 | 0 (0%) |
| Council score too low | 51 | 8 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 39 | 17 | 0 (0%) |
| Top 10 holders own too much | 22 | 7 | 0 (0%) |
| No market yet | 9 | 0 | — |
| Dev wallet already selling | 8 | 3 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Dev holds too much | 2 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 10-31 19:36 | BNB | 84 | Hard stop | $-0.77 |
| 10-31 19:25 | HALLOWEEN | 86 | Trailing stop | $+0.04 |
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
- api.rugcheck.xyz (ConnectionError): 9
