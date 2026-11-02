# Kill-First Desk · paper trading

Updated 2026-11-02 21:25:33 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 282 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $64.14 | $58.42 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 14 | 42 |
| Win rate | 0% | 10% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.92 | $-0.63 |
| Expectancy per trade | $-0.919 | $-0.430 |
| Return per $ bet | -65.3% | -30.6% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 14 and 42).

Lab: 24,632 coins fully tracked for 4 hours, 7,142 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 30,074 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 80 · coins matching the v3 pattern on sight: 116

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 28,964 | 6,447 | 3 (0%) |
| Doesn't match the v3 pattern | 351 | 102 | 1 (1%) |
| Liquidity too low | 155 | 46 | 0 (0%) |
| Top 10 holders own too much | 102 | 33 | 2 (6%) |
| Dev wallet already selling | 53 | 19 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 41 | 10 | 0 (0%) |
| Dev holds too much | 31 | 3 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 6 | 3 | 0 (0%) |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| No holder data | 2 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 0 | — |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 21:13 | PP | 81 | Hard stop | $-0.57 |
| 11-02 20:50 | Caller | 85 | Hard stop | $-0.50 |
| 11-02 20:12 | DELVE | 85 | Trailing stop | $-0.64 |
| 11-02 19:30 | DD | 86 | Hard stop | $-1.29 |
| 11-02 19:06 | Kenneth | 84 | Hard stop | $-0.94 |
| 11-02 16:16 | HUMANIST | 84 | Hard stop | $-0.99 |
| 11-02 15:59 | Nathalia | 88 | Hard stop | $-1.03 |
| 11-02 15:32 | COIN | 86 | Hard stop | $-1.31 |
| 11-02 15:28 | MUCHAN | 98 | Hard stop | $-0.71 |
| 11-02 15:22 | Slingoor | 80 | Hard stop | $-0.23 |
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 2
