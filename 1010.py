# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:40:23 2018

@author: sadra
"""

n=int(input())
x=int(input())
s=n
r=1
while s>=x:
    r=r+1
    s=s//x
A=r*[0]
for i in range(r):
    A[i]=n%x
    n=n//x
while r!=0:
    print(A[r-1])
    r=r-1