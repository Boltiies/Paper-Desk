# Kill-First Desk · paper trading

Updated 2026-11-01 04:34:08 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 508 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $58.19 | $62.43 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 3 |
| Closed trades | 27 | 22 |
| Win rate | 11% | 9% |
| Avg win | $0.53 | $0.48 |
| Avg loss | $-0.86 | $-0.75 |
| Expectancy per trade | $-0.705 | $-0.642 |
| Return per $ bet | -52.1% | -45.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 27 and 22).

Lab: 33,667 coins fully tracked for 4 hours, 4,679 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 44,434 · young coins waiting for a second look: 826 · RugCheck rechecks: 15

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 44,846 | 10,778 | 2 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 160 | 49 | 0 (0%) |
| Fading: few trades in last 5 min | 144 | 47 | 0 (0%) |
| Already pumped this hour | 138 | 34 | 4 (12%) |
| Council score too low | 87 | 23 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 67 | 28 | 0 (0%) |
| Top 10 holders own too much | 47 | 14 | 0 (0%) |
| No market yet | 12 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Dev holds too much | 10 | 5 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 04:27 | Movember | 77 | Hard stop | $-0.99 |
| 11-01 04:08 | NIGUIN | 72 | Hard stop | $-0.66 |
| 11-01 04:04 | YouTube | 90 | Trailing stop | $+0.39 |
| 11-01 03:52 | ELON | 78 | Hard stop | $-0.67 |
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

## Data source errors this run

- lite-api.jup.ag (rate limited): 2
- api.rugcheck.xyz (ConnectionError): 1
