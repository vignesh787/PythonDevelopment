# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:20:41 2021

@author: Vignesh
"""
#__ Use doubleunderscore to mark private membersin a class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    
    def display(self):
        print(self.name,self.age)
        
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks
    
    def display(self):
        super().display()
        print(self.marks)
        
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary
        
    def display(self):
        super().display()
        print(self.salary)
        
        
s = Student('Vignesh',34,7.8)

s.display()

e = Employee('Vignesh',34,1.5)

e.display()