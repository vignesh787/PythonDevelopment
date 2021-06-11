
def initializematrix(dim):
    C=[]
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C


def dot_product(u,v):
    dim=len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i]*v[i])
    return ans

def rowi(M,i):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l
    

def columnj(M,j):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l
    
def mat_mul(A,B):
    dim=len(A)
    C=initializematrix(dim)
    for  i in range(dim):
        for j in range(dim):
            C[i][j]=dot_product(rowi(A,i),columnj(B,j))
    return C


u=[1,2,3]
v=[7,1,2]
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,1],[3,1,7],[6,2,3]]
print(dot_product(u, v))
print(initializematrix(3))
print(mat_mul(A,B))














r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
B=[]
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

c=[[0,0,0],[0,0,0],[0,0,0]]

dim = 3

#C[i][j] is the dot product of ith row of A and jth row of B

for i in range(dim):
    for j in range(dim):
        c[i][j]=c[i][j]+A[i][j]*B[i][j]

#print(c)