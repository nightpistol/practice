import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#create a data frame
df = pd.DataFrame({
  'color':['red','blue','green','green','red','blue']
})
print(df)

#create an instance of OneHotEncoder
encoder = OneHotEncoder()

#fit transform
encoded=encoder.fit_transform(df[['color']]).toarray()

print(encoded)