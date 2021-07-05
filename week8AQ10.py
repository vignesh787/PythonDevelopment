# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:04:52 2021

@author: Vignesh
"""


def checkInequality(n):
    k=0
    for i in range(n):
        if(2**i < n):
            k=i
        else:
            return k
    return k    


#print(checkInequality(10))        
#print(checkInequality(100))   
print(checkInequality(1000))  