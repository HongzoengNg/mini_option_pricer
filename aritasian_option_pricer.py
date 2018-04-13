#  This file implements the Monte Carlo Method with control variate technique
#  for arithmetic asian call/put options
import numpy as np
from scipy.stats import norm

class aritasian_opt(object):
    def __init__(self, future_type, asset_price,mature_time,strike_price,rate,vol,n,path=100000,ctl_var=True):
        if str.upper(future_type) == 'C' or str.upper(future_type) == 'P':
            self.type = str.upper(future_type)
            self.s0=asset_price
            self.K = strike_price
            self.T = mature_time
            self.r = rate
            self.vol = vol*np.sqrt((n+1)*(2*n+1)/(6*n**2))
            self.u = 0.5*self.vol**2+(rate-0.5*vol**2)*(n+1)/(2*n)
            self.val = np.dtype(np.float32)
            self.N = n
            self.path=path
            self.ctl_var=ctl_var
        else:
            print("Type of option is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.s0/self.K)+(self.u+0.5*self.vol**2)*self.T)/(self.vol*np.sqrt(self.T))
        d2 = d1-self.vol*np.sqrt(self.T)
        return d1, d2

    def _cal(self,drift,dt,N,opt_type):
        arit_spath=[]
        geo_spath=[]
        for i in range(self.path):
            s_path=np.array([0]*N)
            Z=np.random.standard_normal(N)
            growthFactor=drift*np.exp(self.vol*np.sqrt(dt)*Z)
            s_path[0]=self.s0*growthFactor[0]
            for i in range(1,N):
                s_path[i]=s_path[i-1]*growthFactor[i]
            aritmean=np.mean(s_path)
            geomean=np.exp((1/N)*np.sum(np.log(s_path)))
            if opt_type=='C':
                arit_spath.append(np.exp(-self.r*self.T)*max(aritmean-self.K,0))
                geo_spath.append(np.exp(-self.r*self.T)*max(geomean-self.K,0))
            else:
                arit_spath.append(np.exp(-self.r*self.T)*max(-aritmean+self.K,0))
                geo_spath.append(np.exp(-self.r*self.T)*max(-geomean+self.K,0))
        # control variate
        arit_spath=np.array(arit_spath)
        geo_spath=np.array(geo_spath)
        Pmean=np.mean(arit_spath)
        Pst=np.std(arit_spath)
        confmc=[Pmean-1.96*Pst/np.sqrt(self.path),Pmean+1.96*Pst/np.sqrt(self.path)]
        covXY=np.mean(arit_spath*geo_spath)-np.mean(arit_spath)*np.mean(geo_spath)
        theta=float(covXY)/np.var(geo_spath)
        return arit_spath,geo_spath,theta,confmc

    def value(self):
        d1,d2 = self.d1_d2()
        N=self.N
        dt=self.T/float(N)
        drift=np.exp((self.r-0.5*self.vol**2)*dt)
        if str.upper(self.type) == 'C':
            geo_c = np.exp(-self.r*self.T)*(self.s0*np.exp(self.u*self.T)*norm.cdf(d1)-self.K*norm.cdf(d2))
            arit_spath,geo_spath,theta,confmc=self._cal(drift,dt,N,self.type)
            if self.ctl_var==True:
                # control version
                Z=arit_spath+theta*(geo_c-geo_spath)
                value=np.mean(Z)
                Zst=np.std(Z)
                confcv=[value-1.96*Zst/np.sqrt(self.path),value+1.96*Zst/np.sqrt(self.path)]
                if str(value)=='nan':
                    self._val=0
                else:
                    self._val=value
                return self._val,confcv
            else:
                value=np.mean(arit_spath)
                if value=='nan':
                    self._val=0
                else:
                    self._val=value
                return self._val,confmc
        elif str.upper(self.type) == 'P':
            geo_c = np.exp(-self.r*self.T)*(self.K*norm.cdf(-d2)-self.s0*np.exp(self.u*self.T)*norm.cdf(-d1))
            arit_spath,geo_spath,theta,confmc=self._cal(drift,dt,N,self.type)
            if self.ctl_var==True:
                # control version
                Z=arit_spath+theta*(geo_c-geo_spath)
                value=np.mean(Z)
                Zst=np.std(Z)
                confcv=[value-1.96*Zst/np.sqrt(self.path),value+1.96*Zst/np.sqrt(self.path)]
                if str(value)=='nan':
                    self._val=0
                else:
                    self._val=value
                return self._val,confcv
            else:
                value=np.mean(arit_spath)
                if value=='nan':
                    self._val=0
                else:
                    self._val=value
                return self._val,confmc