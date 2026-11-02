# Kill-First Desk · paper trading

Updated 2026-11-02 20:24:42 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,671 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $65.22 | $58.64 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 12 | 41 |
| Win rate | 0% | 10% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.98 | $-0.64 |
| Expectancy per trade | $-0.982 | $-0.436 |
| Return per $ bet | -68.8% | -30.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 12 and 41).

Lab: 22,967 coins fully tracked for 4 hours, 6,837 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 27,824 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 78 · coins matching the v3 pattern on sight: 112

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 26,766 | 6,066 | 3 (0%) |
| Doesn't match the v3 pattern | 319 | 94 | 0 (0%) |
| Liquidity too low | 144 | 41 | 0 (0%) |
| Top 10 holders own too much | 99 | 31 | 2 (6%) |
| Dev wallet already selling | 50 | 16 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 41 | 10 | 0 (0%) |
| Dev holds too much | 30 | 2 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 6 | 3 | 0 (0%) |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| No holder data | 2 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 0 | — |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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

- lite-api.jup.ag (rate limited): 4
- api.rugcheck.xyz (ConnectionError): 7
- api.rugcheck.xyz (400): 21
- api.rugcheck.xyz (ReadTimeout): 12
- lite-api.jup.ag (400): 1
