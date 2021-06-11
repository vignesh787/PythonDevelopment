#find minimum most element from list l
#append to a new list l 
#remove the minimum from the original list l 

def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if(l[i]<mini):
            mini=l[i]
    return mini



def obvious_sort(l):
    
    newl = []
    while(len(l)>0):
        mini = min_list(l) 
        newl.append(mini) 
        l.remove(mini)
    return newl

def obvious_sort_old(l):  
   newl = []
   while(len(l) > 0):
       mini = l[0]
       for i in range(len(l)):
           if(l[i]<mini):
               mini=l[i]
       newl.append(mini) 
       l.remove(mini)
   return newl

l=[90,23,97,88,5,1]
print(obvious_sort(l))
l=[90,23,97,88,5,1]
print(obvious_sort_old(l))