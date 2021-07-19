# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:58:41 2021

@author: Vignesh
"""


'''ceaser cipher - shift each letter by 3 '''

import string

def create_caeser_dictionary():
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d