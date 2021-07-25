# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:50:39 2021

@author: Vignesh
"""


class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name  = name
        
    def display(self):
        print(self.roll_no,self.name)
    
s0 = Student(0,'Vignesh')
'''
s0.roll_no = 0
s0.name = 'Vignesh' 

print(s0.roll_no,s0.name)
'''
s0.display()


'''
print(s1.roll_no,s1.name)
'''

s2 = Student(2,'Ganesh')
'''
s2.roll_no = 2
s2.name = 'Ganesh'

print(s2.roll_no,s2.name)
'''

s2.display()