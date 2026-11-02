# Kill-First Desk · paper trading

Updated 2026-11-02 11:24:59 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 472 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $74.31 | $72.92 |
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

Lab: 12,211 coins fully tracked for 4 hours, 3,942 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 9,279 · young coins waiting for a second look: 935 · RugCheck rechecks: 17 · coins matching the v3 pattern on sight: 33

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 10,747 | 2,716 | 1 (0%) |
| Doesn't match the v3 pattern | 116 | 38 | 0 (0%) |
| Top 10 holders own too much | 47 | 12 | 1 (8%) |
| Liquidity too low | 45 | 14 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 19 | 5 | 0 (0%) |
| Dev holds too much | 18 | 2 | 0 (0%) |
| Dev wallet already selling | 11 | 6 | 0 (0%) |
| No market yet | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
