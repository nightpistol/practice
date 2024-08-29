import seaborn as sns

## Basic plotting with seaborn
tips = sns.load_dataset('tips')
print(tips)

#creating a scatterplot
import matplotlib.pyplot as plt
sns.scatterplot(x='total_bill',y='tip',data=tips)
plt.show()

#categorical plots
sns.barplot(x='day',y='total_bill',data=tips)
plt.show()
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()
sns.violinplot(x='day',y='total_bill',data=tips)
plt.show()
sns.histplot(tips['total_bill'],bins=10,kde=True)
plt.show()
sns.pairplot(tips)
plt.show()
corr = tips[['total_bill','tip','size']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
