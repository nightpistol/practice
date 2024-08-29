import pandas as pd

df = pd.DataFrame({
  'color':['red','blue','green','green','red','blue']
})

from sklearn.preprocessing import LabelEncoder,OrdinalEncoder

label_encoder = LabelEncoder()

encoded = label_encoder.fit_transform(df[['color']])
print(encoded)

t = label_encoder.transform([['blue']])
print(t)

df = pd.DataFrame({
  'size':['small','large','medium','medium','large','small']
})
ordinal_en = OrdinalEncoder(categories=[['small','medium','large']])
ord = ordinal_en.fit_transform(df[['size']])

print(ord)