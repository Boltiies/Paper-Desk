#!/usr/bin/env python3
"""
Downloads Coinbase price history (candles) for major coins with ccxt and saves one
gzipped CSV per coin and timeframe in data-cex/coinbase/. Re-running only fetches
what's new. DuckDB can query the files directly, e.g.:

    duckdb -c "select * from 'data-cex/coinbase/BTC-USD-1d.csv.gz' order by ts desc limit 5"

Run:  python cex/fetch_coinbase.py                 (all coins, 1h and 1d, from 2021)
      python cex/fetch_coinbase.py --coins BTC ETH --timeframes 1d
"""
import argparse, os, sys, time
from datetime import datetime, timezone

import ccxt
import pandas as pd

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "data-cex", "coinbase")
COINS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "ADA", "AVAX", "LINK", "LTC", "DOT",
         "BCH", "UNI", "AAVE", "XLM", "ATOM", "NEAR", "SHIB", "SUI"]
START = "2021-01-01"
TF_MS = {"1h": 3_600_000, "1d": 86_400_000}


def fetch(ex, symbol, tf, since_ms):
    rows, since, now_ms = [], since_ms, ex.milliseconds()
    while since < now_ms - TF_MS[tf]:
        for attempt in range(5):
            try:
                batch = ex.fetch_ohlcv(symbol, tf, since=since, limit=300)
                break
            except (ccxt.NetworkError, ccxt.ExchangeError) as e:
                if attempt == 4: raise
                time.sleep(2 * (attempt + 1))
        if not batch:
            since += 300 * TF_MS[tf]          # gap in history (listing date, outage): skip ahead
            continue
        rows += batch
        nxt = batch[-1][0] + TF_MS[tf]
        if nxt <= since: break
        since = nxt
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--coins", nargs="*", default=COINS)
    ap.add_argument("--timeframes", nargs="*", default=["1d", "1h"])
    ap.add_argument("--start", default=START)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    ex = ccxt.coinbase({"enableRateLimit": True})
    ex.load_markets()
    start_ms = int(datetime.fromisoformat(a.start).replace(tzinfo=timezone.utc).timestamp() * 1000)
    failed = []
    for coin in a.coins:
        symbol = f"{coin}/USD"
        if symbol not in ex.markets:
            print(f"{symbol}: not listed on Coinbase, skipped", flush=True); continue
        for tf in a.timeframes:
            path = os.path.join(OUT, f"{coin}-USD-{tf}.csv.gz")
            old = pd.read_csv(path, parse_dates=["ts"]) if os.path.exists(path) else None
            since = int(old["ts"].max().timestamp() * 1000) + TF_MS[tf] if old is not None and len(old) else start_ms
            try:
                rows = fetch(ex, symbol, tf, since)
            except Exception as e:
                print(f"{symbol} {tf}: failed ({e!r})", flush=True); failed.append(f"{symbol} {tf}"); continue
            new = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
            new["ts"] = pd.to_datetime(new["ts"], unit="ms", utc=True)
            df = pd.concat([old, new]) if old is not None else new
            df = df.drop_duplicates("ts").sort_values("ts")
            df = df[df["ts"] < pd.Timestamp.now(tz="UTC").floor("h" if tf == "1h" else "D")]   # drop the unfinished candle
            df.to_csv(path, index=False, compression="gzip")
            print(f"{symbol} {tf}: {len(new):,} new, {len(df):,} total, {df['ts'].min():%Y-%m-%d} to {df['ts'].max():%Y-%m-%d %H:%M}", flush=True)
    if failed:
        print("failed:", ", ".join(failed)); sys.exit(1)


if __name__ == "__main__":
    main()
