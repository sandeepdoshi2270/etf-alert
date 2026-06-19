spmo = {"NVDA": 5, "MSFT": 4, "AMZN": 3}
vfmo = {"NVDA": 3, "AAPL": 6, "MSFT": 2}

common = set(spmo) & set(vfmo)

print("Common holdings:", common)
