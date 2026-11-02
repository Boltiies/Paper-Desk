# Kill-First Desk · paper trading

Updated 2026-11-02 07:09:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 966 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $79.18 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 0 | 5 |
| Win rate | — | 40% |
| Avg win | — | $1.38 |
| Avg loss | — | $-0.38 |
| Expectancy per trade | — | $+0.323 |
| Return per $ bet | — | +21.1% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 5).

Lab: 6,392 coins fully tracked for 4 hours, 5,557 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 4,171 · young coins waiting for a second look: 1,268 · RugCheck rechecks: 12 · coins matching the v3 pattern on sight: 8

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 5,437 | 1,108 | 1 (0%) |
| Doesn't match the v3 pattern | 58 | 18 | 0 (0%) |
| Liquidity too low | 26 | 8 | 0 (0%) |
| Top 10 holders own too much | 23 | 5 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 8 | 0 | — |
| Dev holds too much | 7 | 1 | 0 (0%) |
| Dev wallet already selling | 6 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 12
