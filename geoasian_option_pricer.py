# This file implements closed-form formulas for geometrics Asian call/put options based on black scholes model
import numpy as np
from scipy.stats import norm

class geoasian_opt(object):
    def __init__(self, future_type, asset_price,mature_time,strike_price,rate,vol,n):
        if str.upper(future_type) == 'C' or str.upper(future_type) == 'P':
            self.type = future_type
            self.s0=asset_price
            self.K = strike_price
            self.T = mature_time
            self.r = rate
            self.vol = vol*np.sqrt((n+1)*(2*n+1)/(6*n**2))
            self.u = 0.5*self.vol**2+(rate-0.5*vol**2)*(n+1)/(2*n)
            self.val = np.dtype(np.float32)
        else:
            print("Type of option is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.s0/self.K)+(self.u+0.5*self.vol**2)*self.T)/(self.vol*np.sqrt(self.T))
        d2 = d1-self.vol*np.sqrt(self.T)
        return d1, d2

    def value(self):
        d1,d2 = self.d1_d2()
        if str.upper(self.type) == 'C':
            self.val = np.exp(-self.r*self.T)*(self.s0*np.exp(self.u*self.T)*norm.cdf(d1)-self.K*norm.cdf(d2))
        elif str.upper(self.type) == 'P':
            self.val = np.exp(-self.r*self.T)*(self.K*norm.cdf(-d2)-self.s0*np.exp(self.u*self.T)*norm.cdf(-d1))
        return self.val
