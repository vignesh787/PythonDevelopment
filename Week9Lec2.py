# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:41:11 2021

@author: Vignesh
"""


f=open('numbers.txt','w')
for i in range(10):
    f.write(str(i))
    f.write('\n')
    
f.flush()


f=open('numbers.txt','r')

s='0'
while(s != ''):
    s=f.readline()
    print(s)
