import pandas as pd

# Daily sales log for different stores
data = {
    "date": pd.date_range(start="2026-01-01", periods=6, freq="D").tolist() * 2,
    "store": ["Store_A"] * 6 + ["Store_B"] * 6,
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"] * 2,
    "sales": [100, 200, 150, 250, 300, 180, 80, 120, 110, 190, 210, 150],
}

df = pd.DataFrame(data)
print(df.head())