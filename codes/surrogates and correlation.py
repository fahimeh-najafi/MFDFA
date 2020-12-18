import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt
import cmath as cmath


# RP (random phases surrogate)

def RP(x):
    
    import cmath as cmath
    
    pi=cmath.pi
    l=len(x)
    phi=np.random.uniform(-pi,pi,l)
    
    rpfx=[]
    fx=np.fft.fft(x)
    
    for i in range(l):
        a=cmath.polar(fx[i])
        a=cmath.rect(a[0],phi[i])
        rpfx.append(a)
    
    rpx=np.fft.ifft(rpfx)
    rpx=np.abs(rpx)

    return rpx
    


# RW (Rank Wise surrogate)

def RW(X):
    
    l=len(X)
    N=np.random.normal(0,1,l)
    rwX=np.zeros(l)
    
    Nas=np.argsort(np.argsort(N))
    Xas=np.argsort(np.argsort(X))
    Ns=np.sort(N)
    
    rwX=Ns[Xas]
    
    return rwX



# correlation length calculator in order to compare the correlation after surrogates

def cor(x):
    
    l=len(x)
    tao=int(l/2)

    c=np.zeros(tao)

    for i in range(tao):
        s1=0
        s2=0
        s12=0 
        
        x1=np.array(x[:l-i])
        x2=np.array(x[i:])

        s1=np.mean(x1)
        s2=np.mean(x2)
        s12=np.mean(x1*x2)
    
        c[i]=s12-s1*s2        

    return c
