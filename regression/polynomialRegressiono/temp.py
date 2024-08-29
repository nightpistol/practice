import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values 

# no need for encoding categorical data

#X_train,X_test,y_train,y_test=

#training the model in simple linear regression
lin_regressor=LinearRegression()
lin_regressor.fit(X,y)

#training model into ploynomial regression
pol_regr=PolynomialFeatures(degree=4)
X_poly = pol_regr.fit_transform(X)
lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,y)

#visualising linear
plt.scatter(X,y,color='red')
plt.plot(X,lin_regressor.predict(X),color='blue')
plt.title('truth vs bluff (linear)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#visualising polynomial
plt.scatter(X,y,color='red')
plt.plot(X,lin_reg2.predict(X_poly),color='black')
plt.title('truth vs bluff (poly)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#predicting a new result using linaear and polynomial regres
a=lin_regressor.predict([[6.5]])
b=lin_reg2.predict(pol_regr.fit_transform([[6.5]]))
print(a,b)


