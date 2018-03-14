# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:28:58 2018

@author: sanjeev.ramasamy
"""
w=input()
l=list(w)
c=0
p=0
L=-1
R=1
U=1
D=-1

for i in range(len(w)):
    if l[i]=='L':
        c=c-1
    else:
        if l[i]=='R':
            c=c+1
        else:
            if l[i]=='U':
                c=c+1
            else:
                if l[i]=='D':
                    c=c-1

if c==p:
    print(bool(1))
else:
    print(bool(0))
    
                
            

 
