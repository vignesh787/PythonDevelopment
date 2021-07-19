# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:32:49 2021

@author: Vignesh
"""
#Generator

#similar to function but does not have a return statement

#folowing generator generats square and cube of number 

def square(limit):
    x=0
    while x < limit:
        yield x*x
        yield x*x*x
        x+=1
        
a = square(5)
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))