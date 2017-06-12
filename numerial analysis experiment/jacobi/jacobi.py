import numpy as np

a=np.loadtxt("data.txt")
b=np.matrix(np.loadtxt("const.txt").reshape((3,1)))

def jacobi_iter(x,A,b,step):
    L = np.matrix(np.tril(A,k=-1))
    U = np.matrix(np.triu(A,k=1))
    D = np.matrix(np.diag(np.diag(A)))
    #print(L+U)
    M=np.dot(D.I,-(L+U))
    g=np.dot(D.I,b)
    def improve(x):
        x=np.matrix(x)
        return np.dot(M,x)+g
    def iter(x,step):
        i=1
        x=np.array(x)
        while (i<step):
            print(x)
            x=improve(x)
            i=i+1
        return x
    return iter(x,step)


print(jacobi_iter(np.zeros((3 ,1)),a,b,1000))


