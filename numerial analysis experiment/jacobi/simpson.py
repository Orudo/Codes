def simpsons(fx,a,b):
    n=len(fx)-1
    if(n%2):
        raise ValueError("invalid input--LIST LENGTH MUST BE ODD")
    h=(b-a)/n
    res=fx[0]+fx[-1]
    for i in range(1,n,2):
        res+=4*fx[i]
    for i in range(2,n-1,2):
        res+=2*fx[i]
    return res*h/6

def simpsons(f,a,b,n):    
    if(n%2):
        raise ValueError("value received must be even n=%d",n)
    h=(b-a)/n
    res=f(a)+f(b)
    for i in range(1,n,2):
        res+=4*f(a+i*h)
    for i in range(2,n-1,2):
        res+=2*f(a+i*h)

    return res*h/3


