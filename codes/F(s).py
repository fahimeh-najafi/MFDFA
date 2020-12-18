import numpy as np
import cmath as cmath
from numpy import loadtxt
data = loadtxt("Turb.txt")
n=len(data)


# a function that integrates over our time series

def profile(X):
    
    mX=np.mean(X)
    X=X-mX
    nX=len(X)

    Y=np.zeros((nX))

    # computing profile for our data 
    Y=np.cumsum(X)
        
    
    return Y


Y=profile(data)    
nY=len(Y)


#a function that finds F(s) by inputting a time series, q, s, and degree of fetted polynomial

def F(Y,q,s,deg):
    
 
    n=len(Y)
    ns=int(n/s)
    
    f2=np.zeros((2*ns))
    
    for i in range(ns):
        
        a=np.array((range(i*s,(i+1)*s-1)))
        b=Y[i*s:(i+1)*s-1]
        c = np.polyfit(a, b, deg)
        f = np.poly1d(c)
        y=f(a)
    
        f2[i]=sum( (b-y)**2 )
        
        
        a=np.array((range(n-(i+1)*s,n-i*s-1)))
        b=Y[n-(i+1)*s:n-i*s-1]
        c = np.polyfit(a, b, deg)
        f = np.poly1d(c)
        y=f(a)
    
        f2[i+ns]=sum( (b-y)**2 )
    
    f2=f2/s
        
        
    f=( ( sum( f2**(q/2) ) )/(2*ns) )**(1/q)
    
    return f

    
    
###


ns=4*12+2
s=(np.array(range(ns))+4)/4
s=3**(s+1) 
for i in range(ns):
    s[i]=np.int(s[i])


q=[-6,-5.8,-5.6,-5.4,-5.2,-5,-4.8,-4.6,-4.4,-4.2,-4,-3.8,-3.6,-3.4,
-3.2,-3,-2.8,-2.6,-2.4,-2.2,-2,-1.8,-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,
-0.2,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,
3.6,3.8,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6]

nq=len(q)

# degree of fitted polynomial
d=1

#finding F(s)
f=np.zeros((nq,ns))

for i in range(nq):
    for j in range(ns):
        
        f[i,j]=F(Y,q[i],int(s[j]),d)
        
    print(i)


np.savetxt('f(s).txt', f)


