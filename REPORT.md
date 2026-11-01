# Kill-First Desk · paper trading

Updated 2026-11-01 20:18:17 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 2,431 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $49.81 | $56.64 |
| Started with | $77.00 | $77.00 |
| Open trades | 3 | 4 |
| Closed trades | 54 | 44 |
| Win rate | 15% | 16% |
| Avg win | $0.80 | $0.74 |
| Avg loss | $-0.75 | $-0.70 |
| Expectancy per trade | $-0.523 | $-0.468 |
| Return per $ bet | -42.4% | -36.1% |

## Does the council have an edge?

Council picks return -42.4% per dollar bet, random picks -36.1%. Gap: **-6.4 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 50,189 coins fully tracked for 4 hours, 6,208 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 67,385 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 45

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 65,030 | 16,907 | 7 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 319 | 92 | 0 (0%) |
| Already pumped this hour | 227 | 55 | 6 (11%) |
| Fading: few trades in last 5 min | 218 | 71 | 0 (0%) |
| Council score too low | 160 | 44 | 1 (2%) |
| Top 10 holders own too much | 111 | 36 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 110 | 45 | 0 (0%) |
| No market yet | 32 | 0 | — |
| Dev holds too much | 27 | 8 | 0 (0%) |
| Dev wallet already selling | 20 | 7 | 0 (0%) |
| Too many open trades | 17 | 2 | 0 (0%) |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 17:36 | Leverhedge | 82 | Hard stop | $-0.85 |
| 11-01 17:32 | VETO | 74 | Hard stop | $-0.53 |
| 11-01 17:27 | Sperm | 73 | Hard stop | $-0.76 |
| 11-01 17:09 | GOON | 80 | Hard stop | $-0.91 |
| 11-01 16:30 | RS2s | 80 | Coin died: no buyers | $-0.54 |
| 11-01 15:50 | pairless | 80 | Trailing stop | $+0.65 |
| 11-01 14:57 | Numbat | 71 | Hard stop | $-0.52 |
| 11-01 14:54 | DOGE | 72 | Hard stop | $-0.56 |
| 11-01 14:48 | Alexander | 78 | Hard stop | $-0.77 |
| 11-01 14:29 | REGRETAMINE | 72 | Coin died: no buyers | $-0.40 |
| 11-01 14:07 | Ghost | 72 | Hard stop | $-0.57 |
| 11-01 14:00 | Texocoin | 71 | Hard stop | $-0.64 |
| 11-01 13:55 | BAMF | 76 | Hard stop | $-0.71 |
| 11-01 13:31 | REGRETAMINE | 72 | Trailing stop | $+0.99 |
| 11-01 13:05 | REGRETAMINE | 72 | Hard stop | $-0.70 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 18
