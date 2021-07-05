# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:06:40 2021

@author: Vignesh
"""


def uniq(L):
    m= set()
    for i in range(len(L)):
        m.add(L[i])
    return m


L=[1,2,3,4,5,1,2,3]

print(uniq(L))