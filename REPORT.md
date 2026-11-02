# Kill-First Desk · paper trading

Updated 2026-11-02 07:20:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,004 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $79.74 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 0 | 6 |
| Win rate | — | 33% |
| Avg win | — | $1.38 |
| Avg loss | — | $-0.40 |
| Expectancy per trade | — | $+0.196 |
| Return per $ bet | — | +12.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 6).

Lab: 6,392 coins fully tracked for 4 hours, 5,760 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 4,343 · young coins waiting for a second look: 1,115 · RugCheck rechecks: 12 · coins matching the v3 pattern on sight: 8

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 5,756 | 1,164 | 1 (0%) |
| Doesn't match the v3 pattern | 59 | 19 | 0 (0%) |
| Liquidity too low | 28 | 8 | 0 (0%) |
| Top 10 holders own too much | 24 | 5 | 0 (0%) |
| Dev holds too much | 9 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 8 | 0 | — |
| Dev wallet already selling | 6 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 12
