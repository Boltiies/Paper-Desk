# Kill-First Desk · paper trading

Updated 2026-11-02 04:24:05 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 102 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $77.00 | $77.70 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 0 | 0 |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 0 and 0).

Lab: 3,744 coins fully tracked for 4 hours, 4,772 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 715 · young coins waiting for a second look: 2,445 · RugCheck rechecks: 2 · coins matching the v3 pattern on sight: 0

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 905 | 0 | — |
| Doesn't match the v3 pattern | 12 | 0 | — |
| Liquidity too low | 8 | 0 | — |
| Dev wallet already selling | 3 | 0 | — |
| Dev holds too much | 3 | 0 | — |
| Top 10 holders own too much | 2 | 0 | — |
| Danger flag: Creator history of rugged tokens | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 2
