# # Step 1: Create Sample Raw Data
# import numpy as np
# import pandas as pd

# # Raw Orders Data (contains missing values and noisy strings)
# orders_data = {
#     "order_id": [101, 102, 103, 104, 105, 106, 107],
#     "customer_id": ["C1", "C2", "C1", "C3", "C2", "C4", "C3"],
#     "amount": ["$150.50", " $80.00 ", "$200.00", None, "$50.25", "$300.10", "$120.00"],
#     "order_date": [
#         "2026-01-15",
#         "2026/01/16",
#         "2026-01-18",
#         "2026-01-19",
#         "2026-01-20",
#         "2026-01-21",
#         None,
#     ],
# }

# # Customer Information Data
# customers_data = {
#     "customer_id": ["C1", "C2", "C3", "C4"],
#     "customer_name": ["Alice", "Bob", "Charlie", "David"],
#     "tier": ["Gold", "Silver", "Gold", "Bronze"],
# }

# orders_df = pd.DataFrame(orders_data)
# customers_df = pd.DataFrame(customers_data)

# print("--- Raw Orders ---")
# print(orders_df)
# Step 2: Data Cleaning
# 1. Clean the 'amount' column: strip spaces, remove '$', and convert to float
orders_df["amount"] = (
    orders_df["amount"]
    .str.strip()
    .str.replace("$", "", regex=False)
    .astype(float)
)

# 2. Impute missing 'amount' values with the median order amount
median_amount = orders_df["amount"].median()
orders_df["amount"].fillna(median_amount, inplace=True)

# 3. Convert 'order_date' to standard datetime format and drop invalid rows
orders_df["order_date"] = pd.to_datetime(
    orders_df["order_date"], errors="coerce"
)
orders_df.dropna(subset=["order_date"], inplace=True)

print("--- Cleaned Orders ---")
print(orders_df)