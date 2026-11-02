# Kill-First Desk · paper trading

Updated 2026-11-02 19:20:10 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,293 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $67.15 | $60.64 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 10 | 37 |
| Win rate | 0% | 11% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.99 | $-0.66 |
| Expectancy per trade | $-0.985 | $-0.428 |
| Return per $ bet | -68.1% | -29.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 10 and 37).

Lab: 21,257 coins fully tracked for 4 hours, 6,654 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 25,281 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 78 · coins matching the v3 pattern on sight: 106

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 24,275 | 5,640 | 3 (0%) |
| Doesn't match the v3 pattern | 298 | 78 | 0 (0%) |
| Liquidity too low | 131 | 35 | 0 (0%) |
| Top 10 holders own too much | 96 | 30 | 2 (7%) |
| Dev wallet already selling | 40 | 13 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 40 | 9 | 0 (0%) |
| Dev holds too much | 29 | 2 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 5 | 3 | 0 (0%) |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| No holder data | 2 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 0 | — |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
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
