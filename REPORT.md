# Kill-First Desk · paper trading

Updated 2026-11-03 04:25:36 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 586 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $58.17 | $54.24 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 22 | 49 |
| Win rate | 5% | 8% |
| Avg win | $0.86 | $1.47 |
| Avg loss | $-0.94 | $-0.62 |
| Expectancy per trade | $-0.856 | $-0.449 |
| Return per $ bet | -63.8% | -32.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 22 and 49).

Lab: 36,508 coins fully tracked for 4 hours, 5,473 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 42,308 · young coins waiting for a second look: 2,832 · RugCheck rechecks: 136 · coins matching the v3 pattern on sight: 160

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 40,996 | 9,050 | 3 (0%) |
| Doesn't match the v3 pattern | 503 | 147 | 2 (1%) |
| Liquidity too low | 229 | 70 | 0 (0%) |
| Top 10 holders own too much | 153 | 42 | 3 (7%) |
| Danger flag: Creator history of rugged tokens | 72 | 19 | 0 (0%) |
| Dev wallet already selling | 64 | 27 | 2 (7%) |
| Dev holds too much | 36 | 4 | 0 (0%) |
| No holder data | 29 | 14 | 1 (7%) |
| No market yet | 23 | 0 | — |
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
- api.rugcheck.xyz (ConnectionError): 8
