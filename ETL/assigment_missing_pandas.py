import pandas as pd

# Sample DataFrame
dataOne = {
    'id': [1, 2, None, 3, 5, 6, 6, None, 7],
    'score': [10, None, 20, 30, None, 50, 60, 60, 60],
    'roll': [10, 40, 20, 30, 60, 50, 60, 60, 60],
}

df = pd.DataFrame(dataOne)

for col in df.columns:
    missing_indices = 
    print(df[col].isna().sum())
    # df[col] = df[col].fillna(df[col].shift(1).rolling(3, min_periods=1).mean())

# print("\nDataFrame After Filling Missing Values:\n", df)