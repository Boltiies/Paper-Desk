# Kill-First Desk · paper trading

Updated 2026-11-02 06:15:32 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 680 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $78.94 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 0 | 3 |
| Win rate | — | 0% |
| Avg win | — | $0.00 |
| Avg loss | — | $-0.38 |
| Expectancy per trade | — | $-0.383 |
| Return per $ bet | — | -24.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 3).

Lab: 6,392 coins fully tracked for 4 hours, 4,432 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 3,179 · young coins waiting for a second look: 1,760 · RugCheck rechecks: 10 · coins matching the v3 pattern on sight: 4

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 3,985 | 771 | 1 (0%) |
| Doesn't match the v3 pattern | 46 | 14 | 0 (0%) |
| Top 10 holders own too much | 17 | 3 | 0 (0%) |
| Liquidity too low | 16 | 8 | 0 (0%) |
| Dev wallet already selling | 6 | 3 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 6 | 0 | — |
| Dev holds too much | 5 | 1 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 10
