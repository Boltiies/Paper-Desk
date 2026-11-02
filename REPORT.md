# Kill-First Desk · paper trading

Updated 2026-11-02 02:37:19 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 397 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $51.88 | $53.04 |
| Started with | $77.00 | $77.00 |
| Open trades | 4 | 5 |
| Closed trades | 61 | 54 |
| Win rate | 15% | 15% |
| Avg win | $0.76 | $0.68 |
| Avg loss | $-0.73 | $-0.67 |
| Expectancy per trade | $-0.514 | $-0.471 |
| Return per $ bet | -42.7% | -37.3% |

## Does the council have an edge?

Council picks return -42.7% per dollar bet, random picks -37.3%. Gap: **-5.4 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 60,298 coins fully tracked for 4 hours, 6,305 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 79,878 · young coins waiting for a second look: 2,984 · RugCheck rechecks: 50

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 77,263 | 19,206 | 12 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 389 | 118 | 0 (0%) |
| Fading: few trades in last 5 min | 309 | 106 | 0 (0%) |
| Already pumped this hour | 259 | 74 | 7 (9%) |
| Council score too low | 190 | 57 | 2 (4%) |
| Danger flag: Creator history of rugged tokens | 125 | 49 | 0 (0%) |
| Top 10 holders own too much | 120 | 40 | 1 (2%) |
| No market yet | 41 | 0 | — |
| Dev holds too much | 28 | 8 | 0 (0%) |
| Dev wallet already selling | 25 | 8 | 0 (0%) |
| Too many open trades | 18 | 2 | 0 (0%) |
| Sell test failed (honeypot or no route) | 9 | 2 | 0 (0%) |
| Liquidity not locked or burned | 2 | 2 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 02:04 | F7931A | 73 | Hard stop | $-0.48 |
| 11-02 01:16 | Heidou | 78 | Hard stop | $-1.03 |
| 11-02 00:15 | STEALTH | 76 | Dev wallet sold, got out | $-0.24 |
| 11-02 00:04 | LEARJET | 70 | Trailing stop | $+0.41 |
| 11-01 23:50 | Grok | 90 | Trailing stop | $-0.56 |
| 11-01 22:35 | Amazon | 79 | Dev wallet sold, got out | $-1.12 |
| 11-01 20:19 | CHOO | 85 | Hard stop | $-0.12 |
| 11-01 17:36 | Leverhedge | 82 | Hard stop | $-0.85 |
| 11-01 17:32 | VETO | 74 | Hard stop | $-0.53 |
| 11-01 17:27 | Sperm | 73 | Hard stop | $-0.76 |
| 11-01 17:09 | GOON | 80 | Hard stop | $-0.91 |
| 11-01 16:30 | RS2s | 80 | Coin died: no buyers | $-0.54 |
| 11-01 15:50 | pairless | 80 | Trailing stop | $+0.65 |
| 11-01 14:57 | Numbat | 71 | Hard stop | $-0.52 |
| 11-01 14:54 | DOGE | 72 | Hard stop | $-0.56 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- lite-api.jup.ag (400): 1
