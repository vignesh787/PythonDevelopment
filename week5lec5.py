def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
    
def comp_int(p,n):
    if(n==1):
        return p*(1.1)
    else:
        return comp_int(p,n-1)*1.1