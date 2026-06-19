import json

def fake_holdings(etf):
    if etf == "spmo":
        return [
            {"ticker": "NVDA", "weight": 0.05},
            {"ticker": "MSFT", "weight": 0.04},
        ]
    if etf == "vfmo":
        return [
            {"ticker": "AAPL", "weight": 0.06},
            {"ticker": "NVDA", "weight": 0.03},
        ]

def diff(old, new):
    old_map = {x["ticker"]: x["weight"] for x in old}
    new_map = {x["ticker"]: x["weight"] for x in new}

    added = [t for t in new_map if t not in old_map]
    removed = [t for t in old_map if t not in new_map]

    return added, removed

def run():
    for etf in ["spmo", "vfmo"]:
        old = []  # first run = empty baseline
        new = fake_holdings(etf)

        added, removed = diff(old, new)

        print(f"\n{etf.upper()}")
        print("Added:", added)
        print("Removed:", removed)

run()
