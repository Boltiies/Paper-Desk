# Kill-First Desk · paper trading

Updated 2026-11-02 05:17:31 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 400 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $76.27 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 0 | 3 |
| Win rate | — | 0% |
| Avg win | — | $0.00 |
| Avg loss | — | $-0.38 |
| Expectancy per trade | — | $-0.383 |
| Return per $ bet | — | -24.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 3).

Lab: 5,151 coins fully tracked for 4 hours, 4,442 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 1,867 · young coins waiting for a second look: 2,068 · RugCheck rechecks: 8 · coins matching the v3 pattern on sight: 2

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 2,396 | 383 | 0 (0%) |
| Doesn't match the v3 pattern | 29 | 7 | 0 (0%) |
| Liquidity too low | 15 | 6 | 0 (0%) |
| Top 10 holders own too much | 9 | 1 | 0 (0%) |
| Dev wallet already selling | 5 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 4 | 0 | — |
| Dev holds too much | 3 | 1 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 8
