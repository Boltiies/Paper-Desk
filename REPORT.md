# Kill-First Desk · paper trading

Updated 2026-11-01 00:56:22 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,083 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $63.08 | $64.17 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 5 |
| Closed trades | 19 | 18 |
| Win rate | 11% | 11% |
| Avg win | $0.60 | $0.48 |
| Avg loss | $-0.85 | $-0.77 |
| Expectancy per trade | $-0.702 | $-0.629 |
| Return per $ bet | -49.9% | -44.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 19 and 18).

Lab: 28,524 coins fully tracked for 4 hours, 5,573 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 40,228 · young coins waiting for a second look: 2,916 · RugCheck rechecks: 9

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 38,697 | 9,504 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 126 | 36 | 0 (0%) |
| Fading: few trades in last 5 min | 115 | 37 | 0 (0%) |
| Already pumped this hour | 103 | 27 | 3 (11%) |
| Council score too low | 73 | 21 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 52 | 20 | 0 (0%) |
| Top 10 holders own too much | 41 | 13 | 0 (0%) |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| No market yet | 11 | 0 | — |
| Dev holds too much | 6 | 4 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 00:54 | CASHCAT | 98 | Hard stop | $-0.22 |
| 10-31 23:41 | INKKY | 87 | Hard stop | $-0.94 |
| 10-31 23:37 | CHUDBOB | 84 | Hard stop | $-1.00 |
| 10-31 21:20 | TRACER | 87 | Trailing stop | $-0.87 |
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

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 9
