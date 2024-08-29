import pandas as pd
df = pd.read_csv('winequality-red.csv')
print(df.describe())
print(df.shape)
print(df.columns)
print(df['quality'].unique())
print(df.isnull().sum())
print(df[df.duplicated()])

#check correlation
import seaborn as sns 
import matplotlib.pyplot as plt
sns.heatmap(df.corr(),annot=True)
plt.figure(figsize=(10,6))

#visualisation
print(df.quality.value_counts())

#univariate , bivariate,multivariate analysis
sns.pairplot(df)
