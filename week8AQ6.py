# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:12:17 2021

@author: Vignesh
"""


def is_perfect(selection):
    n = len(selection)
    the_set = set()
    for candidate in selection.values():
        the_set.add(candidate)
        uniq = len(the_set)
    return uniq == n

selection1 = {
'company-1': 'candidate-3',
'company-2': 'candidate-1',
'company-3': 'candidate-2'
}

selection2 = {
'company-1': 'candidate-2',
'company-2': 'candidate-1',
'company-3': 'candidate-2'
}

print(is_perfect(selection1))

print(is_perfect(selection2))
