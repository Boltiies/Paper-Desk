# Kill-First Desk · paper trading

Updated 2026-11-02 06:37:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 802 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $77.68 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 0 | 4 |
| Win rate | — | 25% |
| Avg win | — | $1.26 |
| Avg loss | — | $-0.38 |
| Expectancy per trade | — | $+0.027 |
| Return per $ bet | — | +1.8% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 4).

Lab: 6,392 coins fully tracked for 4 hours, 4,909 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 3,605 · young coins waiting for a second look: 1,619 · RugCheck rechecks: 11 · coins matching the v3 pattern on sight: 5

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 4,537 | 771 | 1 (0%) |
| Doesn't match the v3 pattern | 53 | 14 | 0 (0%) |
| Liquidity too low | 22 | 8 | 0 (0%) |
| Top 10 holders own too much | 19 | 3 | 0 (0%) |
| Dev wallet already selling | 6 | 3 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 6 | 0 | — |
| Dev holds too much | 5 | 1 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 11
