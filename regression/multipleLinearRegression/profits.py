#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#importing dataset
dataset = pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#encoding categorical data
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X=np.array(ct.fit_transform(X))

#dividing datset into training and test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

#training multiple linear regression model
regressor =LinearRegression()
regressor.fit(X_train,y_train)

#predicting test results
y_pred = regressor.predict(X_test) 
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

#to make a single prediction
print(regressor.predict([[1,0,0,160000,130000,300000]]))



