# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:02:02 2021

@author: Vignesh
"""
def is_undirected(mat):
    dim = len(mat)
    for i in range(dim):
        for j in range(dim):
            if(mat[i][j] ==1 && mat[j][i] !=1):
                return False
    return True
        