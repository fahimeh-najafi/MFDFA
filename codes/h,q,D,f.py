import pickle
import numpy as np
import matplotlib.pyplot as plt

from numpy import loadtxt



q=[-6,-5.8,-5.6,-5.4,-5.2,-5,-4.8,-4.6,-4.4,-4.2,-4,-3.8,-3.6,-3.4,-3.2,-3,-2.8,-2.6,-2.4,-2.2,-2,-1.8,-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6]
q=np.array(q)
nq=len(q)
ns=50

nss=4*12+2
s=(np.array(range(nss))+4)/4
s=3**(s+1) 
for i in range(nss):
    s[i]=np.int(s[i])


np.loadtxt('f.txt', f)
np.loadtxt('RPSf.txt', RPSf)
np.loadtxt('RWSf.txt', RWSf)


# finding h(q)

h=np.zeros(nq)
RPSh=np.zeros(nq)
RWSh=np.zeros(nq)

err_h=np.zeros(nq)
err_RPSh=np.zeros(nq)
err_RWSh=np.zeros(nq)

for i in range(nq):
    [slope,intercept],cov=np.polyfit(np.log(s[:24]),np.log(f[i,:24]),1,cov=True)
    h[i]=slope
    
    cov2=np.cov(np.log(s[:24]),np.log(f[i,:24]))
    err_h[i]=np.sqrt(((cov2[1,1]- (cov2[0,1]**2)/cov2[0,0] )/(len(s[:24])-2))/(cov2[0,0]))
    
    [slope,intercept],cov=np.polyfit(np.log(s[:24]),np.log(RPSf[i,:24]),1,cov=True)
    RPSh[i]=slope
    
    cov2=np.cov(np.log(s[:24]),np.log(RPSf[i,:24]))
    err_RPSh[i]=np.sqrt(((cov2[1,1]- (cov2[0,1]**2)/cov2[0,0] )/(len(s[:24])-2))/(cov2[0,0]))
    
    [slope,intercept],cov=np.polyfit(np.log(s[:24]),np.log(RWSf[i,:24]),1,cov=True)
    RWSh[i]=slope
    
    cov2=np.cov(np.log(s[:24]),np.log(RWSf[i,:24]))
    err_RWSh[i]=np.sqrt(((cov2[1,1]- (cov2[0,1]**2)/cov2[0,0] )/(len(s[:24])-2))/(cov2[0,0]))




#finding tau(q) and D(q)
 
tau=np.zeros(nq)
D=np.zeros(nq)
err_tau=np.zeros(nq)

RPStau=np.zeros(nq)
RPSD=np.zeros(nq)
err_RPStau=np.zeros(nq)

RWStau=np.zeros(nq)
RWSD=np.zeros(nq)
err_RWStau=np.zeros(nq)

tau=q*h-1
D=tau/(q-1)
err_tau=q*err_h
err_D=err_tau/(q-1) 
    
    
RPStau=q*RPSh-1
RPSD=RPStau/(q-1)
err_RPStau=q*err_RPSh
err_RPSD=err_RPStau/(q-1) 


RWStau=q*RWSh-1
RWSD=RWStau/(q-1)
err_RWStau=q*err_RWSh
err_RWSD=err_RWStau/(q-1) 


#finding f(alpha)

#derivative of tau(q) is alpha
dtau=np.diff(tau)/0.2
dRPStau=np.diff(RPStau)/0.2
dRWStau=np.diff(RWStau)/0.2

dtau[29]=dtau[29]/2
dRPStau[29]=dRPStau[29]/2
dRWStau[29]=dRWStau[29]/2

f_alpha=np.zeros(len(dtau))
RPS_f_alpha=np.zeros(len(dRPStau))
RWS_f_alpha=np.zeros(len(dRWStau))
        

f_alpha=q[:-1]*(dtau-h[:-1])+1
RPS_f_alpha=q[:-1]*(dRPStau-RPSh[:-1])+1
RWS_f_alpha=q[:-1]*(dRWStau-RWSh[:-1])+1



    



