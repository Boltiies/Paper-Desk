# Kill-First Desk · paper trading

Updated 2026-11-02 12:54:59 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 799 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $74.31 | $68.05 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 3 |
| Closed trades | 2 | 23 |
| Win rate | 0% | 17% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-1.34 | $-0.76 |
| Expectancy per trade | $-1.345 | $-0.372 |
| Return per $ bet | -88.2% | -24.7% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 2 and 23).

Lab: 13,550 coins fully tracked for 4 hours, 4,458 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 11,547 · young coins waiting for a second look: 1,135 · RugCheck rechecks: 21 · coins matching the v3 pattern on sight: 44

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 12,753 | 3,119 | 1 (0%) |
| Doesn't match the v3 pattern | 141 | 38 | 0 (0%) |
| Top 10 holders own too much | 57 | 14 | 1 (7%) |
| Liquidity too low | 55 | 15 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 27 | 6 | 0 (0%) |
| Dev holds too much | 24 | 2 | 0 (0%) |
| Dev wallet already selling | 14 | 6 | 0 (0%) |
| No market yet | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 7
