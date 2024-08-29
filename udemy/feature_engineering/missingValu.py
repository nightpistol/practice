import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print(df.isnull().sum())

# drop columns with null values 
#print(df.dropna(axis=1))

#imputation techniques
#mean imputation for normal distribution
df['age_mean']=df['age'].fillna(df['age'].mean())

#meadian imputation for skewed plots
df['age_meadian']=df['age'].fillna(df['age'].median())

#mode imputation for categoriccal variables
mode_val=df[df['embarked'].notna()]['embarked'].mode()
df['embarked_mode']=df['embarked'].fillna(mode_val)

print(df['embarked'],df['embarked_mode'])

sns.histplot(df['age'],kde=True)
sns.histplot(df['age_mean'],kde=True)
sns.histplot(df['age_meadian'],kde=True)
plt.show()

