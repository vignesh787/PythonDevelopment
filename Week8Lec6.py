import time

def obvious_search(l,k):
    for i in l:
        if(i==k):
            return 1
    return 0

'''print(obvious_search([1,2,3,4,5,6],9))'''

l=list(range(100000000))
k=25000000

a=time.time()
print(obvious_search(l,k))
b=time.time()
print(b-a)