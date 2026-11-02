# Kill-First Desk · paper trading

Updated 2026-11-02 10:04:58 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 113 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $75.75 | $73.78 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 1 | 15 |
| Win rate | 0% | 20% |
| Avg win | $0.00 | $1.63 |
| Avg loss | $-1.25 | $-0.79 |
| Expectancy per trade | $-1.253 | $-0.306 |
| Return per $ bet | -81.4% | -19.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 1 and 15).

Lab: 10,607 coins fully tracked for 4 hours, 4,064 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 7,562 · young coins waiting for a second look: 898 · RugCheck rechecks: 15 · coins matching the v3 pattern on sight: 24

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 9,111 | 2,063 | 1 (0%) |
| Doesn't match the v3 pattern | 95 | 31 | 0 (0%) |
| Top 10 holders own too much | 42 | 10 | 1 (10%) |
| Liquidity too low | 38 | 12 | 0 (0%) |
| Dev holds too much | 16 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 14 | 4 | 0 (0%) |
| Dev wallet already selling | 9 | 4 | 0 (0%) |
| No market yet | 2 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 1
