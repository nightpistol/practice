import numpy as np

list_marks = [10,20,34,56,78,98,54,65,32,99,23,46,73,69,19]
minimum,q1,median,q3,maximum=np.quantile(list_marks,[0,0.25,0.5,0.75,1])
iqr = q3-q1
lower_fence = q1-1.5*iqr
higher_fence = q3 + 1.5*iqr

print(minimum,q1,median,q3,maximum,iqr,lower_fence,higher_fence)

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(list_marks)
plt.show()