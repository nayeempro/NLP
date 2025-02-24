import polars as pl


dataOne = {
    'id': [1,2,None,3,5,6,6,None,7],
    'score':[10,None,20,30,None,50,60,60,60],
    'roll':[10,40,20,30,60,50,60,60,60],
}

df1 = pl.DataFrame(dataOne)
# remove the whole row for null 
df_row = df1.drop_nulls()
# print(df1,df_row)
# give the column which don't have null value
df_col = df1.select([col for col in df1.columns if df1[col].is_not_null().all()])
# print(df_col)

#++++++++++++++++++++++++++++ Imputation method(fil by mean,median,mode)+++++++++++++
df = df1
# check if score col have missing values
df_score = df.select(pl.col('score').is_null().sum())
df_score_all = df.select(pl.col('score').is_not_null().sum())
# remove all missing in score column
df_remove_missing_score = df.filter(pl.col('score').is_not_null())
# remove all missing in id column
df_remove_missing_id = df.filter(pl.col('id').is_not_null())
# print(df_score,df_score_all,df_remove_missing_score,df_remove_missing_id)

# fill null value of score column with mean, median
df_filled_mean = df.with_columns(pl.col('score').fill_null(df['score'].mean()))
df_filled_median = df.with_columns(pl.col('score').fill_null(df['score'].median()))

df_filled_mean_id = df.with_columns(pl.col('id').fill_null(df['id'].mean()))
df_filled_median_id = df.with_columns(pl.col('id').fill_null(df['id'].median()))
# print(df_filled_mean,df_filled_median,df_filled_mean_id,df_filled_median_id)


# +++++++++++++propagation (forward fill/ backward fill)++++++++++++
df_ffill = df.fill_null(strategy='forward')
df_bfill = df.fill_null(strategy='backward')
# print(df,df_ffill,df_bfill)

# fill na with custom value add a new col by 
filledBy50 = df.with_columns(
    pl.when(pl.col('score').is_null())
    .then(pl.lit(50))
    .otherwise(pl.col('score'))
    .alias("fillBy50")
)

print(filledBy50)



