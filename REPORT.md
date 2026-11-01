# Kill-First Desk · paper trading

Updated 2026-11-01 02:42:25 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,842 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $59.97 | $63.07 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 4 |
| Closed trades | 23 | 20 |
| Win rate | 9% | 10% |
| Avg win | $0.60 | $0.48 |
| Avg loss | $-0.87 | $-0.78 |
| Expectancy per trade | $-0.743 | $-0.652 |
| Return per $ bet | -53.8% | -46.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 23 and 20).

Lab: 31,263 coins fully tracked for 4 hours, 5,076 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 42,602 · young coins waiting for a second look: 2,315 · RugCheck rechecks: 13

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 41,588 | 10,105 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 150 | 44 | 0 (0%) |
| Fading: few trades in last 5 min | 137 | 42 | 0 (0%) |
| Already pumped this hour | 120 | 31 | 3 (10%) |
| Council score too low | 79 | 23 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 60 | 23 | 0 (0%) |
| Top 10 holders own too much | 44 | 13 | 0 (0%) |
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

- api.rugcheck.xyz (ConnectionError): 12
- api.rugcheck.xyz (400): 1
