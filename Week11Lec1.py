# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:16:42 2021

@author: Vignesh
"""


a = int(input())
b= int(input())
try:
    c=a/b
    print(c)
    #print(d)
  #  f = open('text.txt','r')
except ZeroDivisionError:
    print('Invalid Input, divisor can not be zero')
except NameError:
    print('Variable not defined')
except FileNotFoundError:
    print('Invalid File Name. Please check again')
except:
    print('Something went wrong')