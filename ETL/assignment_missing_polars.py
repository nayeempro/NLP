import polars as pl

# Sample DataFrame
dataOne = {
    'id': [1, 2, None, 3, 5, 6, 6, None, 7],
    'score': [10, None, 20, 30, None, 50, 60, 60, 60],
    'roll': [10, 40, 20, 30, 60, 50, 60, 60, 60],
}

df = pl.DataFrame(dataOne)
print('original',df)

for col in df.columns:
    # Get the column as a 
    col_series = df[col]
    
    # Find missing value indices
    missing_indices = df[col].is_null().arg_true().to_list()
    

    for i in missing_indices:
        avg = col_series[max(0,i-3):i].mean()
        df = df.with_columns(
                    pl.when(pl.arange(0,df.height)==i)
                    .then(pl.lit(avg))
                    .otherwise(df[col])
                    .alias(col)
            )
            



print(df)

