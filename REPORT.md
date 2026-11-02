# Kill-First Desk · paper trading

Updated 2026-11-02 14:08:31 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 1,308 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $72.74 | $66.27 |
| Started with | $77.00 | $77.00 |
| Open trades | 0 | 5 |
| Closed trades | 3 | 25 |
| Win rate | 0% | 16% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-1.42 | $-0.76 |
| Expectancy per trade | $-1.419 | $-0.408 |
| Return per $ bet | -93.8% | -27.2% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 3 and 25).

Lab: 14,745 coins fully tracked for 4 hours, 4,822 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 13,498 · young coins waiting for a second look: 1,186 · RugCheck rechecks: 22 · coins matching the v3 pattern on sight: 59

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 14,604 | 3,623 | 2 (0%) |
| Doesn't match the v3 pattern | 160 | 41 | 0 (0%) |
| Liquidity too low | 63 | 16 | 0 (0%) |
| Top 10 holders own too much | 63 | 17 | 1 (6%) |
| Danger flag: Creator history of rugged tokens | 28 | 6 | 0 (0%) |
| Dev holds too much | 25 | 2 | 0 (0%) |
| Dev wallet already selling | 24 | 7 | 0 (0%) |
| No market yet | 3 | 0 | — |
| Few huge trades (fake volume?) | 2 | 0 | — |
| Sell test failed (honeypot or no route) | 1 | 0 | — |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 13:08 | PACK | 83 | Dev wallet sold, got out | $-1.57 |
| 11-02 11:09 | SAGE | 86 | Hard stop | $-1.44 |
| 11-02 10:02 | ELON | 88 | Hard stop | $-1.25 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 8
- lite-api.jup.ag (rate limited): 1
