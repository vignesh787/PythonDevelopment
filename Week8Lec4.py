def mini(L):
    mini=L[0]
    for x in L:
        if x < mini:
            mini = x
    return mini

def Sort(L):
    if (L==[] or (len(L) == 1)):
        return L
    m = mini(L)
    L.remove(m)
    return [m]+Sort(L)  

L=[5,6,5,9,12,3,1,2]

print(Sort(L))