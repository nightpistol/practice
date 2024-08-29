import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
print(df.head(5))
print(df.describe())

#to check missing values
print(df.isnull().sum())

#filling missing values with zeroes and storing them
dfa = df.fillna(0)
print(dfa.isnull().sum())

#fill missing values with mean of those values
df['Sales_fillNA'] = df['Sales'].fillna(df['Sales'].mean())
print(df)

#renaming columns
df = df.rename(columns={'Sales_fillNA':'Sales2'})
print(df.head(5))

#change dat types
df['new_values'] = df['Value'].fillna(df['Value'].mean()).astype(int)
print(df)
print(df.dtypes)

#using lambda
df['new_values'] = df['Value'].apply(lambda x:x*2)
print(df)

#data aggregating
grouped_mean = df.groupby('Product')['Value'].mean()
grouped_sum = df.groupby(['Product','Region'])['Value'].sum()
print(grouped_mean,grouped_sum)

#aggregate ultiple functions
grouped_agg = df.groupby('Region')['Value'].agg(['mean','sum','count'])
print(grouped_agg)

#merging and joining data frames

df1 = pd.DataFrame({'Key':['A','B','C'],'Value1':[1,2,3]})
df2 = pd.DataFrame({'Key':['A','B','D'],'Value2':[4,5,6]})

#merging on key column
fuck=pd.merge(df1,df2,on='Key',how='outer')
print(fuck)
