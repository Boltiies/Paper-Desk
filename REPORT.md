# Kill-First Desk · paper trading

Updated 2026-11-02 15:24:02 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 99 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $71.93 | $63.10 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 5 |
| Closed trades | 5 | 29 |
| Win rate | 0% | 14% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.97 | $-0.74 |
| Expectancy per trade | $-0.975 | $-0.440 |
| Return per $ bet | -65.5% | -29.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 5 and 29).

Lab: 16,143 coins fully tracked for 4 hours, 5,217 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 16,250 · young coins waiting for a second look: 1,967 · RugCheck rechecks: 39 · coins matching the v3 pattern on sight: 79

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 16,505 | 4,211 | 3 (0%) |
| Doesn't match the v3 pattern | 195 | 51 | 0 (0%) |
| Top 10 holders own too much | 75 | 21 | 1 (5%) |
| Liquidity too low | 72 | 23 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 30 | 7 | 0 (0%) |
| Dev holds too much | 28 | 2 | 0 (0%) |
| Dev wallet already selling | 27 | 11 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| Sell test failed (honeypot or no route) | 2 | 1 | 0 (0%) |
| No holder data | 1 | 1 | 0 (0%) |
| Sell test: tax or fees too high | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 15:22 | Slingoor | 80 | Hard stop | $-0.23 |
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- lite-api.jup.ag (rate limited): 1
- api.rugcheck.xyz (ConnectionError): 1
