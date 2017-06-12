import NewtonFunction
import math
import random
import numpy
def euler(f,x0,a,b,length):
    print("naive euler function:")
    h=length
    #print(h,n)
    res=x0
    for i in numpy.arange(a,b,length):
        res=res + f(i , res) * h
        print(res)
    return res
#print(euler(lambda x,y:((1/(1+x**2))-2*(y**2)),0,0,2,800))
def improved_euler(f,x0,a,b,length):
    print("improved euler function:")
    h=length
    #print(h,n)
    def k1(x,y): return f(x,y)
    def k2(x,y): return f(x+h,y+h*k1(x,y))
    res=[x0]
    x=[]
    cnt=0
    for i in numpy.arange(a,b,length):
        res.append(res[-1]+(h/2)*(k1(i,res[-1])+k2(i,res[-1])))
        x.append(i)
        print(res[-1])
    x.append(b)

    print(res)
    print(x)
    return [res,x]
#print(improved_euler(lambda x,y:((1/(1+x**2))-2*(y**2)),0,0,2,10))



def bias(x):
    return x-(random.random()-1)/100000
    

def fx(x,y):
    res=4*x/y-x*y
    return res
def diff(f,func,exact,step_length,x0,a,b):
    print("fitting function:")
    func(f,x0,a,b,step_length)
    print("exact solution:")
    for i in numpy.arange(a,b,step_length):
        print(exact(i))
#diff(fx,euler,lambda x:math.sqrt(4+5*math.e**(-x**2)),0.1,3,0,2)
res=improved_euler(fx,3,0,2,0.1)
print(res[0])
print(res[1])
Nx=NewtonFunction.NewtonFunction(res[1],res[0])
def sol(x):
    return math.sqrt(4+5*math.e**(-x**2))

def rank4_R_K(f,x0,a,b,step_length):
    print("Rank 4 Runge-Kutta function:")
    h=step_length
    #print(h,n)
    res=x0
    def k1(x,y): return f(x,y)
    def k2(x,y): return f(x+(h/2),y+(h/2)*k1(x,y))
    def k3(x,y): return f(x+(h/2),y+(h/2)*k2(x,y))
    def k4(x,y): return f(x+h,y+h*k3(x,y))
    for i in numpy.arange(a,b,step_length):
        res=res+(h/6)*(k1(i,res)+2*k2(i,res)+2*k3(i,res)+k4(i,res))
        print(res)
#rank4_R_K(lambda x,y:x**2-y**2,0,-1,0,0.1)


for i in range(1,10000,1):
    ran=(-(random.random()-1))*2
    print("fitting func:")
    print(Nx(ran))
    print("exact:")
    print(sol(ran))