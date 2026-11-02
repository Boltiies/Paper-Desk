# Kill-First Desk · paper trading

Updated 2026-11-02 04:45:36 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 223 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $76.79 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 0 | 1 |
| Win rate | — | 0% |
| Avg win | — | $0.00 |
| Avg loss | — | $-0.78 |
| Expectancy per trade | — | $-0.776 |
| Return per $ bet | — | -50.7% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 1).

Lab: 4,347 coins fully tracked for 4 hours, 4,601 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 1,186 · young coins waiting for a second look: 2,341 · RugCheck rechecks: 5 · coins matching the v3 pattern on sight: 1

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 1,469 | 0 | — |
| Doesn't match the v3 pattern | 18 | 0 | — |
| Liquidity too low | 9 | 0 | — |
| Top 10 holders own too much | 4 | 0 | — |
| Dev wallet already selling | 3 | 0 | — |
| Dev holds too much | 3 | 0 | — |
| Danger flag: Creator history of rugged tokens | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 5
