# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:36:23 2021

@author: Vignesh
"""


fruits = ["mango","apple","orange","watermelon","jackfruit","papaya","litche"]

size = [5,4,6,4,6,2,8]

for fruit in fruits:
    print(fruit)
    
    
for i in range(len(fruits)):
    print(i,fruits[i])
    
    
'''the integer and corresoding value have no real relation ship 
    this is where the enumeration will come to picture'''
    
    
for fruit in (enumerate(fruits)):
    print(fruit)
    
    
print(list(zip(fruits,size)))
print(dict(zip(fruits,size)))