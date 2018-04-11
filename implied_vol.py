import numpy as np
from scipy.stats import norm
import euro_option_pricer as eop

def imp_vol(Type,S0,K,T,r,q,V,tol=1e-8,sigmadiff=1,iter_num=200):
    sigma=np.sqrt(2*abs((np.log(S0/K)+(r-q)*(T))/(T)))
    n=1
    if str.upper(Type)=='C':
        while sigmadiff>=tol and n<iter_num:
            c_bs=eop.euro_opt('C',S0,K,T,sigma,r,q)
            c=c_bs.value()
            d1=c_bs.d1_d2()[0]
            c_vega=S0*np.exp(q*(-T))*np.sqrt(T)*norm.pdf(d1)
            increment=(c-V)/c_vega
            sigma=sigma-increment
            n=n+1
            sigmadiff=abs(increment)
    elif str.upper(Type)=='P':
        while sigmadiff>=tol and n<iter_num:
            p_bs=eop.euro_opt('P',S0,K,T,sigma,r,q)
            p=p_bs.value()
            d1=p_bs.d1_d2()[0]
            p_vega=S0*np.exp(q*(-T))*np.sqrt(T)*norm.pdf(d1)
            increment=(p-V)/p_vega
            sigma=sigma-increment
            n=n+1
            sigmadiff=abs(increment)
    return sigma
