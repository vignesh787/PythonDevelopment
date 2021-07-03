# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:27:00 2021

@author: Vignesh
"""


def placement(p,q):
    if(p==q):
        return 'on'
    if(p<q):
        return 'below'
    if(p>q):
        return 'above'
    
print(placement(3,2))
    