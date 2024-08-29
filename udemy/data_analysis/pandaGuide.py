import pandas as pd
import numpy as np

#series --> 1D data structure
data = [1,2,3,4,5]
series = pd.Series(data)
print('series :\n',series)

#series from dictionary 
data = {'a':1,'b':2,'c':3,'d':4}
series = pd.Series(data)
print(series)

data = [10,20,30]
id = ['a','b','c']
series = pd.Series(data,index=id)
print(series)


#DATA FRAME -> 2D data structure
#creating a dataFrame from dictionary of lists

data = {
'name':['saq','srav','lad'],
'age':[10,20,30],
'city':['bglr','hyd','ncr']
}
df = pd.DataFrame(data)
print(df)
print(np.array(df))

#creating dataFrame from list of dictionaries
data = [
  {'name':'saq','age':20,'city':'hyd'},
  {'name':'saquif','age':23,'city':'hyd'},
  {'name':'saqeded','age':200,'city':'hyd'}
]
df = pd.DataFrame(data)
print(df)

print(df['name'])  # returns name column ... df to series
print(df.loc[1]) #label based
print(df.iloc[:,:-1])  #(row,columns)
print(df.at[1,'age'])

#adding a new column
df['salary'] = [2000,4000,5000]
#removing a column
df.drop('salary',axis=1,inplace=True)