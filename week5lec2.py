def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if(l[i] < mini):
                mini = l[i]
    return mini

def list_max(l):
    maxi = l[0]
    for i in range(len(l)):
        if(l[i] > maxi):
                maxi = l[i]
    return maxi
    
    
def list_appendbefore(l,z):
    newl=[]
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])

    return newl

def list_appendend(l,z):
    newl=[]
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])

    return newl


def list_average(l):
    summ=0
    for i in range(len(l)):
        summ = summ+l[i]
    avg = summ/len(l)
    return avg    
        
l=[1,2,3,4,5,-10,6,4,100]
z=[10,20,40]
print(list_min(l))
print(list_max(l))    
print(list_appendbefore(l, z))
print(list_appendend(l, z))
print(list_average(l))