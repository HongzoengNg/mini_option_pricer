import numpy as np
from scipy.stats import norm

class euro_opt(object):
    def __init__(self, future_type, asset_price, strike_price,  mature_time, vol, rate,repo_q):
        if str.upper(future_type) == 'C' or str.upper(future_type) == 'P':
            self.type = future_type
            self.S = asset_price
            self.K = strike_price
            self.T = mature_time
            self.vol = vol
            self.r = rate
            self.q = repo_q
            self.val = np.dtype(np.float32)
        else:
            print("Type of option is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.S/self.K)+(self.r-self.q)*(self.T))/(self.vol*np.sqrt(self.T)) \
            + 0.5*self.vol*np.sqrt(self.T)
        d2 = (np.log(self.S/self.K)+(self.r-self.q)*(self.T))/(self.vol*np.sqrt(self.T)) \
            - 0.5*self.vol*np.sqrt(self.T)
        return d1, d2

    def value(self):
        d1,d2 = self.d1_d2()
        if str.upper(self.type) == 'C':
            self.val = self.S*np.exp(self.q*(-self.T))*norm.cdf(d1) \
                       - self.K*np.exp(self.r*(-self.T))*norm.cdf(d2)
        elif str.upper(self.type) == 'P':
            self.val = self.K*np.exp(self.r*(-self.T))*norm.cdf(-d2) \
                       - self.S*np.exp(self.q*(-self.T))*norm.cdf(-d1)
        return self.val
