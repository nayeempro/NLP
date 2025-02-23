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
df_remove_missing_score = df.filter(pl.col('score').is_not_null())
df_remove_missing_id = df.filter(pl.col('id').is_not_null())
print(df_score,df_score_all,df_remove_missing_score,df_remove_missing_id)

