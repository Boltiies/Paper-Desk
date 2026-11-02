# Kill-First Desk · paper trading

Updated 2026-11-02 09:54:00 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 56 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $74.54 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 2 |
| Closed trades | 0 | 15 |
| Win rate | — | 20% |
| Avg win | — | $1.63 |
| Avg loss | — | $-0.79 |
| Expectancy per trade | — | $-0.306 |
| Return per $ bet | — | -19.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 15).

Lab: 10,387 coins fully tracked for 4 hours, 4,064 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 7,283 · young coins waiting for a second look: 809 · RugCheck rechecks: 15 · coins matching the v3 pattern on sight: 23

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 8,925 | 1,942 | 1 (0%) |
| Doesn't match the v3 pattern | 93 | 29 | 0 (0%) |
| Top 10 holders own too much | 42 | 9 | 1 (11%) |
| Liquidity too low | 37 | 11 | 0 (0%) |
| Dev holds too much | 16 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 14 | 3 | 0 (0%) |
| Dev wallet already selling | 9 | 4 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 1
