#!/usr/bin/env python3
"""
Reads data/lab.jsonl (every coin that reached the security check, followed for 4 hours)
and writes LEARN.md: which features at decision time went with coins that ran vs died.

A coin "ran" if it reached 2x within 4 hours. It "died" if it had stopped trading by the
4-hour mark. Treat any pattern from fewer than ~200 coins as a hint, not a rule.

Run:  python analyze.py            (uses data/)
      python analyze.py mock-data  (offline test data)
"""
import json, os, sys, statistics as S

base = sys.argv[1] if len(sys.argv) > 1 else "data"
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, base, "lab.jsonl")
rows = [json.loads(l) for l in open(path)] if os.path.exists(path) else []

def last(r):
    s = r["snaps"]; return s[max(s, key=float)] if s else None

for r in rows:
    r["ran"] = r.get("max_x", 0) >= 2
    r["end"] = last(r)
    r["died"] = r["end"] == 0
    r["gate"] = "passed security" if r["verdict"] in ("passed", "bought", "Council score too low", "Fading: few trades in last 5 min",
                                                      "Too many open trades", "Dev wallet already selling") else "failed security"

def line(group, label):
    n = len(group)
    if not n: return None
    ran = sum(r["ran"] for r in group); died = sum(r["died"] for r in group)
    ends = [r["end"] for r in group if r["end"] is not None]
    med = S.median(ends) if ends else 0
    return f"| {label} | {n} | {100*ran/n:.0f}% | {100*died/n:.0f}% | {med:.2f}x |"

def table(title, groups, note=""):
    out = [f"### {title}", ""] + ([note, ""] if note else []) + ["| Group | Coins | Ran 2x+ | Died | Median after 4h |", "|---|---|---|---|---|"]
    out += [l for l in (line(g, lab) for lab, g in groups) if l]
    return out + [""]

def buckets(key, cuts, fmt="{}", pool=None):
    pool = pool if pool is not None else rows
    res = []
    for lo, hi in zip(cuts, cuts[1:]):
        g = [r for r in pool if r["f"].get(key) is not None and lo <= r["f"][key] < hi]
        hi_s = "+" if hi >= 1e8 else fmt.format(hi)
        res.append((f"{fmt.format(lo)} to {hi_s}" if hi < 1e8 else f"{fmt.format(lo)}+", g))
    miss = [r for r in pool if r["f"].get(key) is None]
    if miss: res.append(("unknown", miss))
    return res

L = ["# What the lab learned", "",
     f"{len(rows):,} coins reached the security check and were followed for 4 hours, bought or not. "
     "\"Ran\" means it hit 2x at some point; \"died\" means trading had stopped by 4 hours. "
     "Base rate first, then each feature. Groups under ~50 coins are noise.", ""]
if not rows:
    L += ["No finished coins yet. Each coin takes 4 hours to finish."]
else:
    L += table("Overall", [("All coins", rows)] + [(g, [r for r in rows if r["gate"] == g]) for g in ("passed security", "failed security")])
    verdicts = sorted({r["verdict"] for r in rows}, key=lambda v: -sum(r["verdict"] == v for r in rows))
    L += table("By what the desk decided", [(v, [r for r in rows if r["verdict"] == v]) for v in verdicts],
               "If a kill reason's coins ran as often as the coins it bought, that filter isn't helping.")
    ok = [r for r in rows if r["gate"] == "passed security"]
    L += ["## Coins that passed security", "", f"{len(ok):,} coins. These are the ones the council has to choose between.", ""]
    L += table("Council score", [(lab, [r for r in ok if r.get("score") is not None and lo <= r["score"] < hi])
                                 for lab, lo, hi in (("under 50", 0, 50), ("50 to 60", 50, 60), ("60 to 70", 60, 70), ("70 to 80", 70, 80), ("80+", 80, 999))])
    for key, cuts, fmt, title in [
        ("tx_m5", [0, 5, 15, 40, 100, 1e9], "{:.0f}", "Trades in the last 5 minutes"),
        ("ratio_m5", [0, .45, .55, .65, .75, 1.01], "{:.2f}", "Buy share, last 5 minutes"),
        ("accel", [0, .5, 1, 1.5, 3, 1e9], "{:.1f}", "Speeding up (last 5 min vs hourly pace)"),
        ("ch_m5", [-1e9, -10, 0, 10, 30, 1e9], "{:.0f}%", "Price change, last 5 minutes"),
        ("ch_h1", [-1e9, 0, 50, 100, 200, 1e9], "{:.0f}%", "Price change, last hour"),
        ("ratio_h1", [0, .5, .6, .7, 1.01], "{:.2f}", "Buy share, last hour"),
        ("vol_h24", [0, 4e4, 1e5, 3e5, 1e6, 1e10], "${:,.0f}", "Volume, 24 hours"),
        ("liq", [0, 5e3, 2e4, 5e4, 1e10], "${:,.0f}", "Liquidity"),
        ("mcap", [0, 3e4, 1e5, 3e5, 1e6, 1e10], "${:,.0f}", "Market cap"),
        ("age_min", [0, 15, 60, 240, 1440, 1e9], "{:.0f} min", "Coin age"),
        ("holders", [0, 100, 300, 1000, 3000, 1e9], "{:.0f}", "Holders"),
        ("holders_per_min", [0, 1, 3, 10, 30, 1e9], "{:.0f}", "New holders per minute"),
        ("avg_trade", [0, 20, 50, 150, 500, 1e9], "${:.0f}", "Average trade size, last hour"),
        ("socials", [0, 1, 2, 3, 99], "{:.0f}", "Social links"),
    ]:
        L += table(title, buckets(key, cuts, fmt, ok))
with open(os.path.join(here, base, "LEARN.md") if base != "data" else os.path.join(here, "LEARN.md"), "w") as fh:
    fh.write("\n".join(L) + "\n")
print(f"wrote LEARN.md from {len(rows)} coins")
