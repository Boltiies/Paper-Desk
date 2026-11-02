# Kill-First Desk · paper trading

Updated 2026-11-02 11:35:29 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 518 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $74.31 | $71.37 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 2 | 19 |
| Win rate | 0% | 16% |
| Avg win | $0.00 | $1.63 |
| Avg loss | $-1.34 | $-0.79 |
| Expectancy per trade | $-1.345 | $-0.410 |
| Return per $ bet | -88.2% | -26.9% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 2 and 19).

Lab: 12,362 coins fully tracked for 4 hours, 3,953 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 9,505 · young coins waiting for a second look: 930 · RugCheck rechecks: 17 · coins matching the v3 pattern on sight: 34

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 10,970 | 2,723 | 1 (0%) |
| Doesn't match the v3 pattern | 117 | 38 | 0 (0%) |
| Liquidity too low | 48 | 14 | 0 (0%) |
| Top 10 holders own too much | 48 | 12 | 1 (8%) |
| Dev holds too much | 20 | 2 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 20 | 5 | 0 (0%) |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| No market yet | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
