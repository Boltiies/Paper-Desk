# Kill-First Desk · paper trading

Updated 2026-11-02 15:12:26 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,671 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.35 | $63.26 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 4 | 29 |
| Win rate | 0% | 14% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-1.16 | $-0.74 |
| Expectancy per trade | $-1.162 | $-0.440 |
| Return per $ bet | -77.6% | -29.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 4 and 29).

Lab: 15,928 coins fully tracked for 4 hours, 5,138 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 15,749 · young coins waiting for a second look: 1,750 · RugCheck rechecks: 38 · coins matching the v3 pattern on sight: 77

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 16,234 | 4,022 | 2 (0%) |
| Doesn't match the v3 pattern | 186 | 49 | 0 (0%) |
| Top 10 holders own too much | 75 | 20 | 1 (5%) |
| Liquidity too low | 71 | 21 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 30 | 6 | 0 (0%) |
| Dev holds too much | 28 | 2 | 0 (0%) |
| Dev wallet already selling | 27 | 10 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 1 | 1 | 0 (0%) |
| No holder data | 1 | 0 | — |
| Sell test: tax or fees too high | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 14
- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (400): 10
