# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:00:58 2021

@author: Vignesh
"""
import math

a=[25,-16,49,-100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    if n>=0:
        return n
    
c = map(square_root, filter(is_positive,a))

print(list(c))

