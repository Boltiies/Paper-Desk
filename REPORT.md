# Kill-First Desk · paper trading

Updated 2026-11-02 11:03:00 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 346 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $75.75 | $73.82 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 1 | 16 |
| Win rate | 0% | 19% |
| Avg win | $0.00 | $1.63 |
| Avg loss | $-1.25 | $-0.76 |
| Expectancy per trade | $-1.253 | $-0.314 |
| Return per $ bet | -81.4% | -20.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 1 and 16).

Lab: 11,812 coins fully tracked for 4 hours, 3,933 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 8,807 · young coins waiting for a second look: 938 · RugCheck rechecks: 17 · coins matching the v3 pattern on sight: 28

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 10,283 | 2,401 | 1 (0%) |
| Doesn't match the v3 pattern | 112 | 35 | 0 (0%) |
| Top 10 holders own too much | 45 | 12 | 1 (8%) |
| Liquidity too low | 44 | 12 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 18 | 4 | 0 (0%) |
| Dev holds too much | 16 | 2 | 0 (0%) |
| Dev wallet already selling | 11 | 5 | 0 (0%) |
| No market yet | 3 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
