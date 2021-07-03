# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:31:16 2021

@author: Vignesh
"""


triplets = []

for x in range(1000):
    for y in range(x+1,1000):
        for z in range(y+1,1000):
            z=(x**2 + y**2)**0.5
            if z.is_integer():
                z=int(z)
                if(y<z<1000):
                    triplets.append((x,y,z))    