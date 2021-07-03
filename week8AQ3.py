# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:43:53 2021

@author: Vignesh
"""


def iterativeCompute(n):
    sum=0
    for i in range(n):
        #print(i,2**i)
        sum+=2**i
    return sum


def recursiveCompute(n):
    if(n==1):
        return 1
    else:
        return 2**(n-1) + recursiveCompute(n-1)


print(iterativeCompute(3)) 

print(recursiveCompute(3)) 