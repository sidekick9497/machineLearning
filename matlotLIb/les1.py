import matplotlib.pyplot as plt 
"""
x = [2010,2011,2012,2013]
y = [100,200,150,100]
x2 = [2010.5,2011.5,2012.5,2013.5]
y2 = [123,134,152,235]

plt.bar(x,y, label = "BIg bar")
plt.bar(x2,y2, label ="bar 2", color='#123456')"""

ages = [1,2,1,2,1,1,2,1,2,5,20,21,22,42,42,11,21]
#ids = [1,2,3,4,5,6,7,8]
bins  = [0,10,20,30,40,50,60,70,80,90]
plt.hist(ages,bins,histtype='bar',rwidth=0.8)
plt.show()
