# Kill-First Desk · paper trading

Updated 2026-11-02 15:34:30 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 170 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $70.11 | $62.98 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 7 | 30 |
| Win rate | 0% | 13% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.98 | $-0.73 |
| Expectancy per trade | $-0.985 | $-0.434 |
| Return per $ bet | -66.8% | -29.4% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 7 and 30).

Lab: 16,302 coins fully tracked for 4 hours, 5,388 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 16,695 · young coins waiting for a second look: 2,185 · RugCheck rechecks: 39 · coins matching the v3 pattern on sight: 80

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 16,719 | 4,282 | 3 (0%) |
| Doesn't match the v3 pattern | 201 | 51 | 0 (0%) |
| Liquidity too low | 76 | 23 | 0 (0%) |
| Top 10 holders own too much | 76 | 21 | 1 (5%) |
| Danger flag: Creator history of rugged tokens | 30 | 7 | 0 (0%) |
| Dev wallet already selling | 28 | 11 | 0 (0%) |
| Dev holds too much | 28 | 2 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 2 | 1 | 0 (0%) |
| No holder data | 1 | 1 | 0 (0%) |
| Sell test: tax or fees too high | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 15:32 | COIN | 86 | Hard stop | $-1.31 |
| 11-02 15:28 | MUCHAN | 98 | Hard stop | $-0.71 |
| 11-02 15:22 | Slingoor | 80 | Hard stop | $-0.23 |
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 1
