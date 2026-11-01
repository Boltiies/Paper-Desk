# Kill-First Desk · paper trading

Updated 2026-11-01 01:17:22 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,207 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $62.31 | $63.23 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 5 |
| Closed trades | 20 | 19 |
| Win rate | 10% | 11% |
| Avg win | $0.60 | $0.48 |
| Avg loss | $-0.87 | $-0.79 |
| Expectancy per trade | $-0.726 | $-0.658 |
| Return per $ bet | -51.9% | -46.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 20 and 19).

Lab: 29,032 coins fully tracked for 4 hours, 5,443 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 40,802 · young coins waiting for a second look: 2,909 · RugCheck rechecks: 10

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 39,261 | 9,504 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 132 | 36 | 0 (0%) |
| Fading: few trades in last 5 min | 118 | 37 | 0 (0%) |
| Already pumped this hour | 106 | 27 | 3 (11%) |
| Council score too low | 75 | 21 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 54 | 20 | 0 (0%) |
| Top 10 holders own too much | 42 | 13 | 0 (0%) |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| No market yet | 11 | 0 | — |
| Dev holds too much | 6 | 4 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 01:02 | NNN | 84 | Hard stop | $-1.19 |
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

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 9
- api.rugcheck.xyz (400): 1
