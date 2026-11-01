# Kill-First Desk · paper trading

Updated 2026-11-01 11:37:57 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,420 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $60.97 | $59.18 |
| Started with | $77.00 | $77.00 |
| Open trades | 5 | 4 |
| Closed trades | 34 | 30 |
| Win rate | 12% | 10% |
| Avg win | $0.53 | $0.58 |
| Avg loss | $-0.79 | $-0.71 |
| Expectancy per trade | $-0.638 | $-0.586 |
| Return per $ bet | -48.8% | -43.3% |

## Does the council have an edge?

Council picks return -48.8% per dollar bet, random picks -43.3%. Gap: **-5.5 points**.
A clear, lasting positive gap means the signal is real. Near zero or negative means the council is guessing.

Lab: 40,668 coins fully tracked for 4 hours, 3,317 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 50,839 · young coins waiting for a second look: 856 · RugCheck rechecks: 23

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 51,053 | 13,472 | 5 (0%) |
| No security report | 1,050 | 331 | 3 (1%) |
| Liquidity too low | 213 | 68 | 0 (0%) |
| Already pumped this hour | 169 | 43 | 6 (14%) |
| Fading: few trades in last 5 min | 152 | 50 | 0 (0%) |
| Council score too low | 106 | 31 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 81 | 31 | 0 (0%) |
| Top 10 holders own too much | 70 | 25 | 0 (0%) |
| Dev holds too much | 19 | 6 | 0 (0%) |
| No market yet | 13 | 0 | — |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| Sell test failed (honeypot or no route) | 5 | 1 | 0 (0%) |
| Liquidity not locked or burned | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-01 11:13 | MARVIN | 73 | Trailing stop | $+0.53 |
| 11-01 10:37 | NOGE | 70 | Hard stop | $-0.65 |
| 11-01 10:05 | SCRAT | 70 | Hard stop | $-0.49 |
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

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 3
