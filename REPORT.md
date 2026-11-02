# Kill-First Desk · paper trading

Updated 2026-11-02 22:34:34 UTC. Paper only: no wallet, no real trades.

Dev wallet watch (Helius): **on**, 685 calls this run

## Wallets

| | Council picks | Random control |
|---|---|---|
| Value now | $59.65 | $57.37 |
| Started with | $77.00 | $77.00 |
| Open trades | 1 | 5 |
| Closed trades | 18 | 44 |
| Win rate | 0% | 9% |
| Avg win | $0.00 | $1.47 |
| Avg loss | $-0.96 | $-0.63 |
| Expectancy per trade | $-0.964 | $-0.439 |
| Return per $ bet | -70.2% | -31.5% |

## Does the council have an edge?

Not enough trades yet. Need at least 30 closed trades in each wallet (now 18 and 44).

Lab: 26,530 coins fully tracked for 4 hours, 7,190 still being followed. Run `python analyze.py` to see what predicted the winners (writes LEARN.md).

## Funnel

Coins found: 32,359 · young coins waiting for a second look: 3,000 · RugCheck rechecks: 81 · coins matching the v3 pattern on sight: 128

| Stopped because | Count | Checked 1h later | Pumped 2x+ |
|---|---|---|---|
| Volume too low | 31,193 | 6,927 | 3 (0%) |
| Doesn't match the v3 pattern | 379 | 117 | 2 (2%) |
| Liquidity too low | 166 | 53 | 0 (0%) |
| Top 10 holders own too much | 107 | 36 | 2 (6%) |
| Dev wallet already selling | 56 | 23 | 0 (0%) |
| Danger flag: Creator history of rugged tokens | 43 | 10 | 0 (0%) |
| Dev holds too much | 32 | 4 | 0 (0%) |
| No market yet | 14 | 0 | — |
| Sell test failed (honeypot or no route) | 7 | 3 | 0 (0%) |
| Few huge trades (fake volume?) | 2 | 1 | 0 (0%) |
| No holder data | 2 | 1 | 0 (0%) |
| Liquidity not locked or burned | 2 | 0 | — |
| Sell test: tax or fees too high | 1 | 1 | 0 (0%) |

## Recent council trades

| Closed | Coin | Score | Exit | P&L |
|---|---|---|---|---|
| 11-02 22:27 | GIDGET | 87 | Hard stop | $-1.16 |
| 11-02 21:54 | PWN | 87 | Hard stop | $-1.19 |
| 11-02 21:50 | PWN | 83 | Hard stop | $-0.91 |
| 11-02 21:45 | logan | 89 | Hard stop | $-1.23 |
| 11-02 21:13 | PP | 81 | Hard stop | $-0.57 |
| 11-02 20:50 | Caller | 85 | Hard stop | $-0.50 |
| 11-02 20:12 | DELVE | 85 | Trailing stop | $-0.64 |
| 11-02 19:30 | DD | 86 | Hard stop | $-1.29 |
| 11-02 19:06 | Kenneth | 84 | Hard stop | $-0.94 |
| 11-02 16:16 | HUMANIST | 84 | Hard stop | $-0.99 |
| 11-02 15:59 | Nathalia | 88 | Hard stop | $-1.03 |
| 11-02 15:32 | COIN | 86 | Hard stop | $-1.31 |
| 11-02 15:28 | MUCHAN | 98 | Hard stop | $-0.71 |
| 11-02 15:22 | Slingoor | 80 | Hard stop | $-0.23 |
| 11-02 14:40 | MAYA | 99 | Dev wallet sold, got out | $-0.39 |

## Data source errors this run

- api.rugcheck.xyz (ConnectionError): 3
- mainnet.helius-rpc.com (ConnectionError): 1
- lite-api.jup.ag (rate limited): 2
