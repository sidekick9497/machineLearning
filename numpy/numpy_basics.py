import numpy as np 
a = np.array([[1,2,3],[23,23,23]] ,ndmin=2,dtype=np.int32)
b = [4,2,3,4,5]
dt =  np.dtype([('Name','S20'),('Age','i1')])
custom = np.array([('harry',21)],dtype=dt)
print(a.shape)
a.shape = (3,2)
print(a.shape)
print(a.itemsize)
print(a.flags)
zerosnp = np.ones((3,2))
print(zerosnp)
c = np.asarray(b)
print(c.shape)