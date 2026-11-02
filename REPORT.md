# Kill-First Desk · paper trading

Updated 2026-11-02 08:40:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,385 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $83.68 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 0 | 10 |
| Win rate | — | 30% |
| Avg win | — | $1.63 |
| Avg loss | — | $-0.54 |
| Expectancy per trade | — | $+0.112 |
| Return per $ bet | — | +7.3% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 10).

Lab: 8,850 coins fully tracked for 4 hours, 4,511 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 5,925 · young coins waiting for a second look: 916 · RugCheck rechecks: 13 · coins matching the v3 pattern on sight: 14

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 7,498 | 1,557 | 1 (0%) |
| Doesn't match the v3 pattern | 73 | 22 | 0 (0%) |
| Liquidity too low | 34 | 9 | 0 (0%) |
| Top 10 holders own too much | 33 | 8 | 1 (12%) |
| Dev holds too much | 14 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 12 | 0 | — |
| Dev wallet already selling | 7 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 13
