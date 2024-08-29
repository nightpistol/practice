import numpy as np

#creating a 1d array in numpy
arr1 = np.array([1,2,3,4,5,6])
print(arr1)

#reshaping it into 2d array
arr2 = arr1.reshape(2,3)  #(row,column)
print(arr2)
print(arr2[1][1])

#arrayRange
print(np.arange(0,10,2))

#all matrix elements are 1
print(np.ones((4,4)))

#identity matrix 
print(np.eye(3))


#VECTOR OPERATIONS
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,4,3,2,1])

#element wise operations
print('addition:',arr1+arr2)
print('multiplication:',arr1*arr2)

#universal functions
arr = np.array([1,2,3,4,5])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))

#array slicing and indexing
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #two brackets
print(arr[1:,1:-1])

#normalisation
#to have mean of 0 and standard deviation of 1

data = np.array([1,2,3,4,5])
mean = np.mean(data)
std_dev = np.std(data)

#normalise the data
normalised_data = (data-mean)/std_dev
print('normalised data:',normalised_data)

#logical operators
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data>5)
print(data[(data>5) & (data<9)])