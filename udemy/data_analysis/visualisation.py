import pandas as pad
import matplotlib.pyplot as plt

#creating a line plot
x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.plot(x,y,color='red',linestyle='--',marker='o')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line plot')
plt.show()

#multiple plots
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2 = [2,4,6,8,10]

plt.figure(figsize=(9,5))
plt.subplot(2,2,1)
plt.plot(x,y1,color='red')

plt.subplot(2,2,2)
plt.plot(x,y2,color='blue')

plt.subplot(2,2,3)
plt.plot(x,y1,color='green')

plt.subplot(2,2,4)
plt.plot(x,y2,color='gray')

plt.show()

# Bar Plots
cate = ['a','b','c','d','e']
val = [2,3,4,5,6]

plt.bar(cate,val,color='blue')
plt.show()

#histograms
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data,bins=5,color='red',edgecolor='black')
plt.show()

#scatterplot
x=[1,2,3,4,5]
y = [2,3,4,5,6]
plt.scatter(x,y,color='pink',marker='*')
plt.show()

#pie chart
labels = ['A','B','C','D']
sizes = [10,20,30,40]
colors = ['green','gray','skyblue','indigo']
explode = (0,0,0,0.2)#move out  specified slice

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
plt.show()