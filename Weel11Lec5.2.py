# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:55:07 2021

@author: Vignesh
"""


#list comprehension

fruits = ["apple","orange","pineapple","watermelon","grapes","banana","sweetline","lemon"]

newList=[]
'''
for fruit in fruits:
    if 'n' in fruit:
        newList.append(fruit.upper())
'''

newList = [fruit.capitalize() for fruit in fruits if 'n' in fruit ]
print(newList)