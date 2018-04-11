# This file implements closed-form formulas for geometrics basket call/put options based on black scholes model
import numpy as np
from scipy.stats import norm

class geobasket_opt(object):
    def __init__(self, future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol):
        if str.upper(future_type) == 'C' or str.upper(future_type) == 'P':
            self.type = future_type
            self.bg0 = np.sqrt(asset_price1*asset_price2)
            self.K = strike_price
            self.T = mature_time
            self.r = rate
            self.rol = rol
            self.vol_b = np.sqrt(vol1**2+vol2**2+2*rol*vol1*vol2)/2
            self.u_b = rate-(vol1**2+vol2**2)/4+0.5*(self.vol_b**2)
            self.val = np.dtype(np.float32)
        else:
            print("Type of option is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.bg0/self.K)+(self.u_b+0.5*self.vol_b**2)*self.T)/(self.vol_b*np.sqrt(self.T))
        d2 = d1-self.vol_b*np.sqrt(self.T)
        return d1, d2

    def value(self):
        d1,d2 = self.d1_d2()
        if str.upper(self.type) == 'C':
            self.val = np.exp(-self.r*self.T)*(self.bg0*np.exp(self.u_b*self.T)*norm.cdf(d1)-self.K*norm.cdf(d2))
        elif str.upper(self.type) == 'P':
            self.val = np.exp(-self.r*self.T)*(self.K*norm.cdf(-d2)-self.bg0*np.exp(self.u_b*self.T)*norm.cdf(-d1))
        return self.val
