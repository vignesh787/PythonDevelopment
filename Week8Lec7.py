# -*- coding: utf-8 -*-
def binarySearch(L,k):
    midpoint = int(len(L)/2)
    ret=0
    print(L[midpoint],k,midpoint)
    if( k == L[midpoint]):
        print("Comparision",k,L[midpoint])
        return 1
    elif( k < L[midpoint]):
        N = L[0:midpoint]
        print(N)
        if(N!=[]):
            return binarySearch(N,k)
        else:
            return 0
    elif(k > L[midpoint]):
        M=L[midpoint+1:len(L)]
        print(M)
        if(M!=[]):
            return binarySearch(M,k) 
        else:
            return 0
           
L=[0,2,4,6,8,10,12,14,16,18,20]
k=23

print(binarySearch(L,k))
        
        