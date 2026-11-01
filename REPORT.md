# Kill-First Desk · paper trading

Updated 2026-11-01 02:16:21 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,708 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $60.79 | $63.26 |
| Started with | $77.00 | $77.00 |
| Open trades | 2 | 5 |
| Closed trades | 22 | 19 |
| Win rate | 9% | 11% |
| Avg win | $0.60 | $0.48 |
| Avg loss | $-0.87 | $-0.79 |
| Expectancy per trade | $-0.732 | $-0.658 |
| Return per $ bet | -52.8% | -46.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 22 and 19).

Lab: 30,552 coins fully tracked for 4 hours, 5,275 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 42,147 · young coins waiting for a second look: 2,584 · RugCheck rechecks: 11

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 40,880 | 9,890 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 145 | 40 | 0 (0%) |
| Fading: few trades in last 5 min | 131 | 40 | 0 (0%) |
| Already pumped this hour | 117 | 30 | 3 (10%) |
| Council score too low | 78 | 22 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 59 | 22 | 0 (0%) |
| Top 10 holders own too much | 44 | 13 | 0 (0%) |
| No market yet | 12 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Dev holds too much | 6 | 5 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
| 10-31 16:45 | DOUGHBRIKS | 70 | Hard stop | $-0.72 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 10
- api.rugcheck.xyz (400): 1
