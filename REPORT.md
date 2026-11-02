# Kill-First Desk · paper trading

Updated 2026-11-02 08:55:31 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,480 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $76.69 |
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

Lab: 9,118 coins fully tracked for 4 hours, 4,446 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 6,208 · young coins waiting for a second look: 875 · RugCheck rechecks: 13 · coins matching the v3 pattern on sight: 16

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 7,816 | 1,579 | 1 (0%) |
| Doesn't match the v3 pattern | 75 | 22 | 0 (0%) |
| Top 10 holders own too much | 35 | 8 | 1 (12%) |
| Liquidity too low | 34 | 9 | 0 (0%) |
| Dev holds too much | 15 | 1 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 13 | 0 | — |
| Dev wallet already selling | 7 | 3 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 13
- lite-api.jup.ag (ConnectionError): 1
