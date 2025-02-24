import polars as pl

# Sample DataFrame
dataOne = {
    'id': [1, 2, None, 3, 5, 6, 6, None, 7],
    'score': [10, None, 20, 30, None, 50, 60, 60, 60],
    'roll': [10, 40, 20, 30, 60, 50, 60, 60, 60],
}

df = pl.DataFrame(dataOne)
print("Original DataFrame:\n", df)

# Iterate over each column
for col in df.columns:
    col_series = df[col].to_list()  # Convert to list for modification
    
    # Find missing value indices
    missing_indices = [i for i, val in enumerate(col_series) if val is None]

    for i in missing_indices:
        # Get previous 3 values (including newly replaced ones)
        prev_values = [col_series[j] for j in range(max(0, i - 3), i) if col_series[j] is not None]

        if prev_values:  # Only replace if we have at least one valid value
            avg = sum(prev_values) / len(prev_values)
            col_series[i] = avg  # Update list directly

    # Reassign updated column back to DataFrame and cast to original dtype
    df = df.with_columns(pl.Series(col, col_series).cast(df[col].dtype))

print("\nUpdated DataFrame:\n", df)
