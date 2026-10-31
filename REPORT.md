# Kill-First Desk · paper trading

Updated 2026-10-31 21:10:09 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 2,178 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.41 | $68.06 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 3 |
| Closed trades | 15 | 15 |
| Win rate | 13% | 7% |
| Avg win | $0.60 | $0.36 |
| Avg loss | $-0.88 | $-0.79 |
| Expectancy per trade | $-0.687 | $-0.712 |
| Return per $ bet | -48.0% | -49.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 15 and 15).

Lab: 23,201 coins fully tracked for 4 hours, 5,676 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 33,776 · young coins waiting for a second look: 3,000

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 32,327 | 7,980 | 2 (0%) |
| No security report | 1,050 | 330 | 3 (1%) |
| Liquidity too low | 81 | 17 | 0 (0%) |
| Already pumped this hour | 79 | 16 | 3 (19%) |
| Fading: few trades in last 5 min | 71 | 19 | 0 (0%) |
| Council score too low | 56 | 9 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 41 | 17 | 0 (0%) |
| Top 10 holders own too much | 27 | 7 | 0 (0%) |
| Dev wallet already selling | 9 | 4 | 0 (0%) |
| No market yet | 9 | 0 | — |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Dev holds too much | 3 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 0 | — |

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
- api.rugcheck.xyz (ConnectionError): 10
