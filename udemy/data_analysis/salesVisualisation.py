import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales1_data.csv')
#total sales by products
sales_group=data.groupby('Product')['Sales'].sum()
sales_group.plot(kind='bar',color='green')
plt.xlabel('products')
plt.ylabel('sales')
plt.show()