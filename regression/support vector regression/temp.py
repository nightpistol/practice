import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values
y=y.reshape(len(y),1)  #as feature scaling takes 2d array as input

#feature scaling as salaries are very big compared to positions 
scX=StandardScaler()
scY=StandardScaler()
#we can't use same method for both because when invoking standard method it creates mean and standard deviation for that particular dataset ..... so diff dataset hence another StandardScaler()
X=scX.fit_transform(X)
y=scY.fit_transform(y)

#training on svr model
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

#predicting a salary
sal = scY.inverse_transform(regressor.predict(scX.transform([[6.5]])).reshape(-1,1))
print(sal)

#visualising Svr result
plt.scatter(scX.inverse_transform(X),scY.inverse_transform(y),color='red')
plt.plot(scX.inverse_transform(X),scY.inverse_transform(regressor.predict(X).reshape(-1,1)),color='blue')
plt.title('truth vs bluff (SVR)')
plt.xlabel('experience')
plt.ylabel('salary')
plt.show()

