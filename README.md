# Kill-First Desk · paper trading

A paper trader for new Solana memecoins. It watches live coins, runs the same
checks and exits the real bot would, and records what would have happened.
**No wallet, no keys, no real money.**

Results: open **REPORT.md**. It updates every few minutes while a run is going
and is saved to this repo at the end of each run.

## What it measures

Two paper wallets start with $77 each:

- **Council picks** buys only coins that pass every safety check *and* score 70+.
- **Random control** buys a random sample of coins that passed the safety checks,
  ignoring the score.

If the council's picks keep beating the random ones, the scoring has a real edge.
If not, it's guessing. Give it at least 30 closed trades in each wallet,
ideally a few hundred, before drawing conclusions.

## How it runs

GitHub runs `paper_trader.py` every 6 hours for about 5h40m (see
`.github/workflows/paper.yml`). Start a run any time from the **Actions** tab:
**Paper desk → Run workflow**.

Keep this repository **public**: GitHub gives public repos free run time, and
there's nothing secret in here.

## Data sources

- DexScreener: new token profiles and boosts, prices, volume, trades
- pump.fun: newest coins (unofficial endpoint, may be blocked at times)
- RugCheck: mint/freeze authority, holders, insiders, LP lock, risk flags
- Jupiter: buy and sell quotes, used for the sell test and for realistic fills
  (includes exchange fees and price impact). Priority fee and Jito tip are added on top.
  The free endpoint is used by default. If it ever stops working, add a free key from
  Jupiter as a repository secret named `JUP_API_KEY`. Until then the bot falls back to
  estimated fills and says so at the top of the report.

- Helius (optional, free key as repository secret `HELIUS_API_KEY`): watches the coin
  creator's wallet. Skips coins whose dev is already selling and sells a position
  as soon as the dev sells. The key never appears in logs.

Young coins with no market yet, or too little volume, get a second look after
3, 10 and 30 minutes. `data/api-debug.txt` shows the first answer from each data
source in the latest run.

## Rules

Edit `CFG` at the top of `paper_trader.py`. Defaults match the tuned simulator:
2% bets, max 5 open trades, 40% daily loss limit, −40% stop, 25% sold at +150%,
50% trailing stop on the rest, council score 70+.

## Council v2 and the lab (from 30 Oct 2026)

The first council (v1) ran for 62 closed trades and did no better than random
picks: about -27% per dollar bet in both wallets. Its results are saved in
`data/archive-v1.json`.

Version 2 scores coins on the last 5 minutes instead of the last hour, since
1-hour numbers couldn't tell rising coins from fading ones. It skips coins with
fewer than 15 trades in the last 5 minutes, and checks open trades every 20
seconds even during long scouting passes.

**The lab** follows every coin that gets a live market, including ones dropped for low volume,
and records its price 5, 15, 30, 60, 120 and 240 minutes later in `data/lab.jsonl`.
That gives hundreds of labeled coins a day instead of a few dozen trades.
`python analyze.py` writes `LEARN.md`, showing which features went with coins
that hit 2x and which went with coins that died.

## Council v3 (from 2 Nov 2026)

Council v2 did no better than random picks (archived in `data/archive-v2.json`).
Across 62,024 lab coins, judged only on the numbers available when each coin
was first seen, one pattern held up in both halves of the data: buys making up
75%+ of the last 5 minutes of trades, price up over the last hour, market cap
$10k-$300k, and the coin under an hour old. 28% of matching coins doubled within
4 hours, against 1.5% of all coins. About 116 coins a day match.

v3 buys only that pattern, and checks matching coins the moment they're seen
instead of waiting for $40k volume. The "already pumped this hour" filter and
the social score are gone. The random control wallet still buys a random sample
of coins that pass security, so the two wallets show whether the pattern beats
chance after fees. Rough estimates from the lab still came out at about -11% per
trade, so this is a test, not a sure thing.
