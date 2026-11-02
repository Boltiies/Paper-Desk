# Kill-First Desk · paper trading

Updated 2026-11-02 16:11:27 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 342 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $69.08 | $62.01 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 8 | 31 |
| Win rate | 0% | 13% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.99 | $-0.73 |
| Expectancy per trade | $-0.990 | $-0.445 |
| Return per $ bet | -67.6% | -30.3% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 8 and 31).

Lab: 17,048 coins fully tracked for 4 hours, 5,607 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 18,187 · young coins waiting for a second look: 2,775 · RugCheck rechecks: 41 · coins matching the v3 pattern on sight: 84

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 17,586 | 4,403 | 3 (0%) |
| Doesn't match the v3 pattern | 218 | 51 | 0 (0%) |
| Liquidity too low | 88 | 23 | 0 (0%) |
| Top 10 holders own too much | 79 | 22 | 1 (5%) |
| Danger flag: Creator history of rugged tokens | 30 | 7 | 0 (0%) |
| Dev wallet already selling | 29 | 11 | 0 (0%) |
| Dev holds too much | 28 | 2 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 2 | 1 | 0 (0%) |
| No holder data | 2 | 1 | 0 (0%) |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 15:59 | Nathalia | 88 | Hard stop | $-1.03 |
| 11-02 15:32 | COIN | 86 | Hard stop | $-1.31 |
| 11-02 15:28 | MUCHAN | 98 | Hard stop | $-0.71 |
| 11-02 15:22 | Slingoor | 80 | Hard stop | $-0.23 |
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 3
