# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:55:48 2018

@author: sanjeev.ramasamy
"""
l=[6,1,8,6,8]

count=0

for d in range(len(l)-1):
    m=l[d]
    n=l[d+1]
    a=list("{0:b}".format(m))
    b=list("{0:b}".format(n))
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

a=list("{0:b}".format(l[0]))
b=list("{0:b}".format(l[len(l)-1]))
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