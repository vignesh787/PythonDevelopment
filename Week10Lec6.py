# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:58:26 2021

@author: Vignesh
"""


import matplotlib.pyplot as plt
import numpy as np 

x = np.array([3,5,6,3,4,5,6,7,2,4,1,8,9,6])

y = np.array([23,56,78,34,6,98,63,25,15,77,89,12,45,87])

plt.scatter(x,y)

plt.bar(x,y)

plt.show()