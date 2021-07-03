# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:25:44 2021

@author: Vignesh
"""


def is_shrinking(sequence):
    flag=False
    for i in range(len(sequence)-1):
        if((sequence[i]-sequence[i+1])>0):
            flag=True
        else:
            flag=False
            return False
    return flag
        

L=[100,50,52,35,33,32]

print(is_shrinking(L))
    