# Kill-First Desk · paper trading

Updated 2026-11-02 14:45:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,562 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.35 | $63.87 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 4 | 28 |
| Win rate | 0% | 14% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-1.16 | $-0.77 |
| Expectancy per trade | $-1.162 | $-0.448 |
| Return per $ bet | -77.6% | -30.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 4 and 28).

Lab: 15,428 coins fully tracked for 4 hours, 4,971 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 14,702 · young coins waiting for a second look: 1,479 · RugCheck rechecks: 36 · coins matching the v3 pattern on sight: 69

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 15,483 | 3,896 | 2 (0%) |
| Doesn't match the v3 pattern | 175 | 47 | 0 (0%) |
| Liquidity too low | 69 | 20 | 0 (0%) |
| Top 10 holders own too much | 69 | 18 | 1 (6%) |
| Danger flag: Creator history of rugged tokens | 30 | 6 | 0 (0%) |
| Dev wallet already selling | 25 | 9 | 0 (0%) |
| Dev holds too much | 25 | 2 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 1 | 1 | 0 (0%) |
| No holder data | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 12
- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (400): 10
