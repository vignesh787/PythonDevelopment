# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 07:44:18 2021

@author: Vignesh
"""

#ax1+by1+c=0 
#ax2+by2c=0

#given a,b,c for both equation solve for x and y 

def solve(eq1,eq2):
    print(eq1,eq2)
    sub = [];
    eq1xcoeff = eq1[0];
    eq2xcoeff = eq2[0]
    #Multiple eq1 withx co-efficient of eq2
    for i in range(len(eq1)):
        eq1[i]=eq1[i]*eq2xcoeff
    #Multiple eq2 withx co-efficient of eq1    
    for i in range(len(eq2)):
        eq2[i]=eq2[i]*eq1xcoeff
        
    #subtract both matrix to cancelx co-efficient and compute y coefficient 
    print(eq1,eq2)    
    for i in range(len(eq1)):
        sub.insert(i,eq1[i]-eq2[i])

    #compute y
    y = -sub[2]/sub[1]
  #  print(int(y)) 
    
    y = int(y)
    
    x=-(eq1[1]*y + eq1[2])/eq1[0]
    
    x=int(x)
    
   # print(int(x))
    
    print(x,y)  
    
    return(int(x),int(y))


#solve([1,-2,6],[3,5,-15])

#solve([10,-4,-58],[6,4,10])

#solve([2,-1,-3],[3,2,1])

solve([-3,2,34],[5,-3,-56])