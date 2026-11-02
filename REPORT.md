# Kill-First Desk · paper trading

Updated 2026-11-02 04:35:01 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 166 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $77.79 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 0 | 0 |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 0).

Lab: 4,075 coins fully tracked for 4 hours, 4,692 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 942 · young coins waiting for a second look: 2,357 · RugCheck rechecks: 4 · coins matching the v3 pattern on sight: 1

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 1,213 | 0 | — |
| Doesn't match the v3 pattern | 16 | 0 | — |
| Liquidity too low | 8 | 0 | — |
| Top 10 holders own too much | 4 | 0 | — |
| Dev wallet already selling | 3 | 0 | — |
| Dev holds too much | 3 | 0 | — |
| Danger flag: Creator history of rugged tokens | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 4
