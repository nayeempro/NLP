import pandas as pd

data = {
    'id': [1,2,2,3,4,5,6,6,7],
    'score':[10,20,20,30,40,50,60,60,60]
}

# convert dataframe (1st step)
df = pd.DataFrame(data)
print("original data",df)
#detect duplicated row (detect last + keep first)
df_duplicate_data = df[df.duplicated()]
# print(df_duplicate_data)

#detect duplicated row (detect first+keep last)
df_duplicate_data = df[df.duplicated(keep="last")]
# print(df_duplicate_data)

#remove duplicated Data (keep last and delete first)
new_data = df.drop_duplicates(keep="last")
print(new_data)