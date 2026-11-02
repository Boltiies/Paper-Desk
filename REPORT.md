# Kill-First Desk · paper trading

Updated 2026-11-02 14:55:30 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,595 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.35 | $63.66 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 4 | 29 |
| Win rate | 0% | 14% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-1.16 | $-0.74 |
| Expectancy per trade | $-1.162 | $-0.440 |
| Return per $ bet | -77.6% | -29.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 4 and 29).

Lab: 15,621 coins fully tracked for 4 hours, 5,033 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 15,110 · young coins waiting for a second look: 1,559 · RugCheck rechecks: 37 · coins matching the v3 pattern on sight: 73

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 15,801 | 3,896 | 2 (0%) |
| Doesn't match the v3 pattern | 180 | 47 | 0 (0%) |
| Top 10 holders own too much | 71 | 18 | 1 (6%) |
| Liquidity too low | 70 | 20 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 30 | 6 | 0 (0%) |
| Dev holds too much | 27 | 2 | 0 (0%) |
| Dev wallet already selling | 25 | 9 | 0 (0%) |
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

- api.rugcheck.xyz (ConnectionError): 13
- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (400): 10
