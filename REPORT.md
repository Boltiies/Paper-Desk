# Kill-First Desk · paper trading

Updated 2026-11-03 03:16:42 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 278 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $58.17 | $56.54 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 22 | 46 |
| Win rate | 5% | 9% |
| Avg win | $0.86 | $1.47 |
| Avg loss | $-0.94 | $-0.62 |
| Expectancy per trade | $-0.856 | $-0.436 |
| Return per $ bet | -63.8% | -31.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 22 and 46).

Lab: 34,804 coins fully tracked for 4 hours, 5,668 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 40,501 · young coins waiting for a second look: 2,872 · RugCheck rechecks: 134 · coins matching the v3 pattern on sight: 151

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 39,226 | 8,580 | 3 (0%) |
| Doesn't match the v3 pattern | 471 | 142 | 2 (1%) |
| Liquidity too low | 208 | 66 | 0 (0%) |
| Top 10 holders own too much | 139 | 39 | 2 (5%) |
| Danger flag: Creator history of rugged tokens | 66 | 16 | 0 (0%) |
| Dev wallet already selling | 62 | 26 | 2 (8%) |
| Dev holds too much | 35 | 4 | 0 (0%) |
| No holder data | 29 | 2 | 0 (0%) |
| No market yet | 22 | 0 | — |
| Sell test failed (honeypot or no route) | 7 | 3 | 0 (0%) |
| Few huge trades (fake volume?) | 3 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 0 | — |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-03 01:48 | OnlyCats | 94 | Dev wallet sold, got out | $-1.30 |
| 11-02 23:04 | Crime | 86 | Trailing stop | $+0.86 |
| 11-02 22:40 | logitechs | 89 | Dev wallet sold, got out | $-0.77 |
| 11-02 22:40 | COW | 69 | Dev wallet sold, got out | $-0.25 |
| 11-02 22:27 | GIDGET | 87 | Hard stop | $-1.16 |
| 11-02 21:54 | PWN | 87 | Hard stop | $-1.19 |
| 11-02 21:50 | PWN | 83 | Hard stop | $-0.91 |
| 11-02 21:45 | logan | 89 | Hard stop | $-1.23 |
| 11-02 21:13 | PP | 81 | Hard stop | $-0.57 |
| 11-02 20:50 | Caller | 85 | Hard stop | $-0.50 |
| 11-02 20:12 | DELVE | 85 | Trailing stop | $-0.64 |
| 11-02 19:30 | DD | 86 | Hard stop | $-1.29 |
| 11-02 19:06 | Kenneth | 84 | Hard stop | $-0.94 |
| 11-02 16:16 | HUMANIST | 84 | Hard stop | $-0.99 |
| 11-02 15:59 | Nathalia | 88 | Hard stop | $-1.03 |

## Data source errors this run

- api.rugcheck.xyz (400): 3
- api.rugcheck.xyz (ConnectionError): 6
