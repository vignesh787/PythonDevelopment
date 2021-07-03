# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:06:15 2021

@author: Vignesh
"""

def recMulFunction(a,b):
    if(b==1):
        return a
    else:
        return a+recMulFunction(a,(b-1))

def iterMulFunction(a,b):
    sum=0
    for i in range(b):
        sum+=a
    return sum

print(iterMulFunction(27,6))

print(recMulFunction(27,6))
