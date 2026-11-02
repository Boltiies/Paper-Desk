# Kill-First Desk · paper trading

Updated 2026-11-02 09:31:58 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,559 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $76.11 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 0 | 14 |
| Win rate | — | 21% |
| Avg win | — | $1.63 |
| Avg loss | — | $-0.72 |
| Expectancy per trade | — | $-0.214 |
| Return per $ bet | — | -13.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 14).

Lab: 9,914 coins fully tracked for 4 hours, 4,168 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 6,871 · young coins waiting for a second look: 826 · RugCheck rechecks: 14 · coins matching the v3 pattern on sight: 22

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 8,513 | 1,942 | 1 (0%) |
| Doesn't match the v3 pattern | 82 | 29 | 0 (0%) |
| Top 10 holders own too much | 39 | 9 | 1 (11%) |
| Liquidity too low | 35 | 11 | 0 (0%) |
| Dev holds too much | 16 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 14 | 3 | 0 (0%) |
| Dev wallet already selling | 8 | 4 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 14
- lite-api.jup.ag (ConnectionError): 1
