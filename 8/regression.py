import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data=pd.read_csv('LR.csv',header=None)
dim=data.shape

xsum=0
for i in data[0]:
    xsum+=i
xmean=xsum/dim[0]
ysum=0
for i in data[1]:
    ysum+=i
ymean=ysum/dim[0]

x1=[i-xmean for i in data[0]]
y1=[i-ymean for i in data[1]]

x2=[pow(i,2) for i in x1]
xy=[]
for i in range(len(x1)):
    xy.append(x1[i]*y1[i])

b1=sum(xy)/sum(x2)

b0=ymean-b1*xmean
x=data[0]
y=data[1]
plt.plot(x,y,'ro')
xn=int(input("Enter value of x:"))
yn=b1*xn+b0
print("Value of y:",yn)

plt.plot(xn,yn,marker='o',color='blue',markersize=10)
b=np.array(range(min(data[0]),max(data[0])))
c=b0+b1*b
plt.plot(b,c)
plt.show()



    

    

