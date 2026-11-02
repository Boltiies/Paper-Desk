# Kill-First Desk · paper trading

Updated 2026-11-02 21:15:03 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 225 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $64.14 | $58.47 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 14 | 41 |
| Win rate | 0% | 10% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.92 | $-0.64 |
| Expectancy per trade | $-0.919 | $-0.436 |
| Return per $ bet | -65.3% | -30.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 14 and 41).

Lab: 24,325 coins fully tracked for 4 hours, 7,105 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 29,634 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 79 · coins matching the v3 pattern on sight: 116

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 28,532 | 6,311 | 3 (0%) |
| Doesn't match the v3 pattern | 347 | 99 | 1 (1%) |
| Liquidity too low | 154 | 44 | 0 (0%) |
| Top 10 holders own too much | 101 | 33 | 2 (6%) |
| Dev wallet already selling | 52 | 18 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 41 | 10 | 0 (0%) |
| Dev holds too much | 30 | 3 | 0 (0%) |
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

- api.rugcheck.xyz (ConnectionError): 1
