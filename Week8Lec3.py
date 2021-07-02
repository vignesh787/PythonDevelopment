def check0(L):
    if(len(L)==0):
        return '0'
    if(L[0]==0):
        return '1'
    else:
       return check0(L[1:len(L)])
                
ans=(check0([1,2,0,4,5,10,8,7,3]))

print(ans)