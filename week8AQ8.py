# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:36:21 2021

@author: Vignesh
"""


def remainder(a, b):
    if a < b:
        return a
    return remainder(a - b, b)