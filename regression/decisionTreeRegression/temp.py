import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)

ans=regressor.predict([[6.5]])
print(ans)

X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('truth vs bluff (decision tree)')
plt.xlabel('exp')
plt.ylabel('salary')
plt.show()