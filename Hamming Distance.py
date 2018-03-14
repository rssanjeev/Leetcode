# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:55:48 2018

@author: sanjeev.ramasamy
"""
x=1
y=4

count=0
a=list("{0:b}".format(x))
b=list("{0:b}".format(y))
if(len(a)>len(b)):
    max=a
    min=b
else:
    max=b
    min=a
diff=len(max)-len(min)

for i in range(diff):
    min.insert(0,'0')

for i in range(len(max)):
    
    if(max[i]!=min[i]):
        count+=1

print(count)