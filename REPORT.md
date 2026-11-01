# Kill-First Desk · paper trading

Updated 2026-11-01 08:27:39 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 2,197 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $56.40 | $59.84 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 2 |
| Closed trades | 31 | 27 |
| Win rate | 10% | 7% |
| Avg win | $0.53 | $0.48 |
| Avg loss | $-0.81 | $-0.72 |
| Expectancy per trade | $-0.680 | $-0.632 |
| Return per $ bet | -51.3% | -46.1% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 31 and 27).

Lab: 38,231 coins fully tracked for 4 hours, 3,106 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 47,844 · young coins waiting for a second look: 647 · RugCheck rechecks: 20

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 48,355 | 12,264 | 4 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 184 | 59 | 0 (0%) |
| Already pumped this hour | 155 | 39 | 6 (15%) |
| Fading: few trades in last 5 min | 147 | 48 | 0 (0%) |
| Council score too low | 98 | 26 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 73 | 29 | 0 (0%) |
| Top 10 holders own too much | 56 | 17 | 0 (0%) |
| Dev holds too much | 15 | 5 | 0 (0%) |
| No market yet | 13 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Sell test failed (honeypot or no route) | 4 | 0 | — |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 08:08 | niketyson | 88 | Hard stop | $-0.70 |
| 11-01 06:17 | GLIPUP | 78 | Coin died: no buyers | $-0.17 |
| 11-01 06:07 | Solana | 87 | Hard stop | $-0.69 |
| 11-01 05:50 | GTA 6 Coin | 72 | Hard stop | $-0.48 |
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

## Data source errors this run

- lite-api.jup.ag (rate limited): 2
- api.rugcheck.xyz (ConnectionError): 6
