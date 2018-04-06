import numpy as np 
height = np.round(np.random.normal(1.75,0.50,30),2)
weight = np.round(np.random.normal(65,10,30),2)
data = np.column_stack((height,weight))
data2 = np.row_stack((height,weight))
print data.shape
print data2.shape
mean = np.mean(data[:,0])
print mean
