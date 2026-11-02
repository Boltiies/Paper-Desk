# Kill-First Desk · paper trading

Updated 2026-11-02 07:41:32 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,066 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $79.12 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 2 |
| Closed trades | 0 | 8 |
| Win rate | — | 25% |
| Avg win | — | $1.38 |
| Avg loss | — | $-0.46 |
| Expectancy per trade | — | $+0.004 |
| Return per $ bet | — | +0.3% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 8).

Lab: 6,392 coins fully tracked for 4 hours, 6,062 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 4,732 · young coins waiting for a second look: 910 · RugCheck rechecks: 13 · coins matching the v3 pattern on sight: 11

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 6,337 | 1,164 | 1 (0%) |
| Doesn't match the v3 pattern | 64 | 19 | 0 (0%) |
| Liquidity too low | 32 | 8 | 0 (0%) |
| Top 10 holders own too much | 26 | 5 | 0 (0%) |
| Dev holds too much | 11 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 8 | 0 | — |
| Dev wallet already selling | 6 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 13
