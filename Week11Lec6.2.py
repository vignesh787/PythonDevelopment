# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:54:29 2021

@author: Vignesh
"""


a=[4,6,2,5,4,8,4,6]
b=[7,4,2,5,6,7,8,2]

def sub(a,b):
    return a-b


#map function takes 2 arguments. first one is the funciton name
    # and remaining are the parameters 

c=map(sub,a,b)
print(list(c))

#map filter function