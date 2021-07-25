# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:53:52 2021

@author: Vignesh
"""


import numpy as np

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a, a.ndim, '\n')  #ndim - dimention gets printed
print(b, b.ndim, '\n')
print(c, c.ndim, '\n')
print(d, d.ndim, '\n')