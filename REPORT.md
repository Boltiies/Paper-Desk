# Kill-First Desk · paper trading

Updated 2026-11-01 03:14:22 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,966 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $59.83 | $62.78 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 3 |
| Closed trades | 23 | 21 |
| Win rate | 9% | 10% |
| Avg win | $0.60 | $0.48 |
| Avg loss | $-0.87 | $-0.77 |
| Expectancy per trade | $-0.743 | $-0.651 |
| Return per $ bet | -53.8% | -46.3% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 23 and 21).

Lab: 32,018 coins fully tracked for 4 hours, 4,856 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 43,161 · young coins waiting for a second look: 1,856 · RugCheck rechecks: 14

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 42,584 | 10,274 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 155 | 46 | 0 (0%) |
| Fading: few trades in last 5 min | 142 | 43 | 0 (0%) |
| Already pumped this hour | 124 | 32 | 3 (9%) |
| Council score too low | 81 | 23 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 65 | 25 | 0 (0%) |
| Top 10 holders own too much | 45 | 14 | 0 (0%) |
| No market yet | 12 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Dev holds too much | 6 | 5 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 02:30 | Reaper | 79 | Hard stop | $-0.98 |
| 11-01 02:14 | PUTIN | 80 | Hard stop | $-0.72 |
| 11-01 01:54 | BLUE | 82 | Hard stop | $-0.86 |
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

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 13
- api.rugcheck.xyz (400): 1
