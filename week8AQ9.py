# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:37:24 2021

@author: Vignesh
"""


import random
L = [ ]
for i in range(25):
    L.append(random.randint(1, 100))
    

def average(L):
    S = 0
    for mark in L:
        S += mark
    return S / len(L)

def insert(x, L):
    out_L = [ ]
    inserted = False
    for elem in L:
        if not inserted and x < elem:
            out_L.append(x)
            inserted = True
            out_L.append(elem)
            if not inserted:
                out_L.append(x)
    return out_L

def sort(L):
    if len(L) <= 1:
        return L
    return insert(L[0], sort(L[1:]))

def median(L):
    sorted_L = sort(L)
    # for odd number of elements
    mid = len(sorted_L) // 2
    return sorted_L[mid]


