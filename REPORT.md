# Kill-First Desk · paper trading

Updated 2026-11-02 09:06:31 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,489 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $76.85 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 1 |
| Closed trades | 0 | 13 |
| Win rate | — | 23% |
| Avg win | — | $1.63 |
| Avg loss | — | $-0.70 |
| Expectancy per trade | — | $-0.163 |
| Return per $ bet | — | -10.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 13).

Lab: 9,326 coins fully tracked for 4 hours, 4,386 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 6,406 · young coins waiting for a second look: 881 · RugCheck rechecks: 14 · coins matching the v3 pattern on sight: 19

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 8,002 | 1,723 | 1 (0%) |
| Doesn't match the v3 pattern | 77 | 25 | 0 (0%) |
| Top 10 holders own too much | 37 | 8 | 1 (12%) |
| Liquidity too low | 35 | 11 | 0 (0%) |
| Dev holds too much | 15 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 14 | 1 | 0 (0%) |
| Dev wallet already selling | 7 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 14
- lite-api.jup.ag (ConnectionError): 1
