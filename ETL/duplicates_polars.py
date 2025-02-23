import polars as pl

data = {
    'id': [1,2,2,3,4,5,6,6,7],
    'score':[10,20,20,30,40,50,60,60,60]
}

dataOne = {
    'id': [1,2,2,3,5,6,6,7,7],
    'score':[10,20,20,30,40,50,60,60,60],
}

df = pl.DataFrame(data)
df1 = pl.DataFrame(dataOne)

# Detect for row  with boolean
df1_duplicate_data = df1.with_columns(df1.is_duplicated())
# print("duplicated data",df1_duplicate_data)
df1_duplicate_data_filter = df1.filter(df1.is_duplicated())
print("duplicated data",df1_duplicate_data_filter)

# detect according to column
id_duplicates = df.group_by('id').count()
# print("duplicated_id",id_duplicates)
score_duplicates = df.group_by('score').count()
# print("duplicated_score",score_duplicates)



# Remove duplicate data 

# remove duplicates keeping fast
df_unique = df.unique()
# remove duplicates in column score
df_unique_score = df.unique(subset=['score'],maintain_order=True)
df_unique_order_keep_last = df.unique(maintain_order=True,keep="last")
# print(df_unique,df_unique_score,df_unique_order_keep_last)
df_aggregated = df.group_by("id").agg(pl.col("score").first())
print("df_aggregated",df_aggregated)


# Summary Table
# Method	Description
# is_duplicated()	Detects duplicate rows, excluding the first occurrence
# with_columns(df.is_duplicated().alias("is_duplicate"))	Adds a new column indicating duplicates
# filter(df.is_duplicated())	Returns only duplicate rows
# unique()	Removes duplicate rows while keeping the first occurrence
# unique(subset=["col"])	Removes duplicates based on a specific column
# filter(~df.is_duplicated(keep="both"))	Removes all occurrences of duplicates


