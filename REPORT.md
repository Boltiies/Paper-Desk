# Kill-First Desk · paper trading

Updated 2026-11-02 11:14:00 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 428 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $74.31 | $74.37 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 4 |
| Closed trades | 2 | 17 |
| Win rate | 0% | 18% |
| Avg win | $0.00 | $1.63 |
| Avg loss | $-1.34 | $-0.73 |
| Expectancy per trade | $-1.345 | $-0.315 |
| Return per $ bet | -88.2% | -20.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 2 and 17).

Lab: 12,063 coins fully tracked for 4 hours, 3,911 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 9,088 · young coins waiting for a second look: 975 · RugCheck rechecks: 17 · coins matching the v3 pattern on sight: 31

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 10,518 | 2,562 | 1 (0%) |
| Doesn't match the v3 pattern | 116 | 38 | 0 (0%) |
| Top 10 holders own too much | 46 | 12 | 1 (8%) |
| Liquidity too low | 45 | 13 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 19 | 4 | 0 (0%) |
| Dev holds too much | 17 | 2 | 0 (0%) |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| No market yet | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
