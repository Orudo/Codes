import numpy as np
def get_diff_quot(xi,fi):
    if(len(xi)>2 and len(fi)>2):
        return ((get_diff_quot(xi[1:len(xi)],fi[1:len(fi)])-get_diff_quot(xi[:len(xi)-1],fi[:len(fi)-1]))/float(xi[-1]-xi[0]))
    return (fi[1]-fi[0])/float(xi[1]-xi[0])

def generate_omega(i,xi):
    def Wi(x):
        res=1.0;
        for index in range(i):
            res=res*(x-xi[index])
        return res
    return Wi

def NewtonFunction(xi,fi):
    def iter(x):
        res=fi[0]
        for i in range(2,len(xi)):
            res+=generate_omega(i-1,xi)(x)*get_diff_quot(xi[:i],fi[:i])
        return res
    return iter

sr_x = [i for i in range(-50, 51, 10)]
sr_fx = [i**2+2*i+1 for i in sr_x]
Nx=NewtonFunction(sr_x,sr_fx)


x=[i for i in np.linspace(-50.0,51.0,1000)]
fx=[Nx(i) for i in x]
for i in range(1000):
    print(str(x[i])+" "+str(fx[i]))
print(Nx(-1))