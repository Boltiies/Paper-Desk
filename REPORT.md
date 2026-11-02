# Kill-First Desk · paper trading

Updated 2026-11-02 08:29:31 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,325 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $84.86 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 0 | 9 |
| Win rate | — | 33% |
| Avg win | — | $1.63 |
| Avg loss | — | $-0.46 |
| Expectancy per trade | — | $+0.240 |
| Return per $ bet | — | +15.7% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 9).

Lab: 8,667 coins fully tracked for 4 hours, 4,530 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 5,667 · young coins waiting for a second look: 864 · RugCheck rechecks: 13 · coins matching the v3 pattern on sight: 13

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 7,298 | 1,557 | 1 (0%) |
| Doesn't match the v3 pattern | 72 | 22 | 0 (0%) |
| Liquidity too low | 34 | 9 | 0 (0%) |
| Top 10 holders own too much | 29 | 8 | 1 (12%) |
| Dev holds too much | 13 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 12 | 0 | — |
| Dev wallet already selling | 7 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 13
