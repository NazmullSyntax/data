def process_data(df):
    """Add store-level sales metrics to a DataFrame."""
    # Sort by date to ensure proper window order
    df = df.sort_values(by=["store", "date"])

    # 1. Cumulative Sum per Store
    df["running_total"] = df.groupby("store")["sales"].cumsum()

    # 2. Rolling 3-Day Moving Average per Store
    df["3_day_moving_avg"] = (
        df.groupby("store")["sales"]
        .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
    )

    # 3. Dense Rank sales within each store (highest sale = rank 1)
    df["sales_rank"] = df.groupby("store")["sales"].rank(method="dense", ascending=False)

    print(df[["date", "store", "sales", "running_total", "3_day_moving_avg", "sales_rank"]])
    return df