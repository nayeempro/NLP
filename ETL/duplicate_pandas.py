import pandas as pd

data = {
    'id': [1,2,2,3,4,5,6,6,7],
    'score':[10,20,20,30,40,50,60,60,60]
}

dataOne = {
    'id': [1,2,2,3,5,6,6,7,7],
    'score':[10,20,30,30,40,50,60,60,60],
}

# convert dataframe (1st step)
df = pd.DataFrame(data)
dfOne = pd.DataFrame(dataOne)
print("original data",df)
# +++++++++++++++duplicates_row+++++++++++++++++++++++++++++
#detect duplicated row (detect last + keep first)
df_duplicate_data = df[df.duplicated()]
# print(df_duplicate_data)

#detect duplicated row (detect first+keep last)
df_duplicate_data = df[df.duplicated(keep="last")]
# print(df_duplicate_data)

#remove duplicated Data (keep last and delete first)
new_data = df.drop_duplicates(keep="last")
# print(new_data)


# +++++++++++++++++duplicates col data ++++++++++++++

# detect duplicates in col"id"
col_duplicates_id = dfOne[dfOne.duplicated(subset=['id'])] 
print(col_duplicates_id)
# detect duplicates in col"score"
col_duplicates_score = dfOne[dfOne.duplicated(subset=['score'])] 
print(col_duplicates_score)

#remove duplicated Data (according to id column)
new_data_id = df.drop_duplicates(subset="id")
print(new_data_id)

#remove duplicated Data (according to id column)
new_data_score = df.drop_duplicates(subset="score")
print(new_data_score)

# Find the frequency of each value in a column

freq_id = df['id'].value_counts()
print(freq_id)

# Count occurrences of each ID
freq_id_groupBy = df.groupby('id').size().reset_index(name='count')
print('freq by groupby',freq_id_groupBy)