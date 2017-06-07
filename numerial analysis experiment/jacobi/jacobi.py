import numpy as np

a=np.loadtxt("data.txt")
b=np.matrix(np.loadtxt("const.txt").reshape((3,1)))

print(b)

L=np.matrix(np.tril(a,k=-1))
U=np.matrix(np.triu(a,k=1))
D=np.matrix(np.diag(np.diag(a)))
print(L+U)
M=np.dot(D.I,-(L+U))
g=np.dot(D.I,b)

print(M)
print(g)


def improve(x):
    x=np.matrix(x)
    return np.dot(M,x)+g

def jacobi_iter(x,step):
    i=1
    x=np.array(x)
    while (i<step):
        print(x)
        x=improve(x)
        i=i+1
    return x

print(jacobi_iter(np.zeros((3 ,1)),1000))


