#  This file implements the Monte Carlo Method with control variate technique
#  for arithmetic mean basket call/put options
import numpy as np
from scipy.stats import norm

class aritbasket_opt(object):
    def __init__(self, future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol,path=100000,ctl_var=True):
        if str.upper(future_type) == 'C' or str.upper(future_type) == 'P':
            self.type = future_type
            self.s1_0=asset_price1
            self.s2_0=asset_price2
            self.bg0 = np.sqrt(asset_price1*asset_price2)
            self.K = strike_price
            self.T = mature_time
            self.r = rate
            self.rol = rol
            self.vol1 = vol1
            self.vol2 = vol2
            self.vol_b = np.sqrt(vol1**2+vol2**2+2*rol*vol1*vol2)/2
            self.u_b = rate-(vol1**2+vol2**2)/4+0.5*(self.vol_b**2)
            self._val = np.dtype(np.float32)
            self.path=path
            self.ctl_var=ctl_var
        else:
            print("Type of option is invalid.\nPlease input with \'call\' or \'put\'.")

    def d1_d2(self):
        d1 = (np.log(self.bg0/self.K)+(self.u_b+0.5*self.vol_b**2)*self.T)/(self.vol_b*np.sqrt(self.T))
        d2 = d1-self.vol_b*np.sqrt(self.T)
        return d1, d2

    def _cal(self,drift1,drift2,dt,N,opt_type):
        arit_spath=[]
        geo_spath=[]
        for i in range(self.path):
            s1_path=np.array([0]*N)
            s2_path=np.array([0]*N)
            Z1=np.random.standard_normal(N)
            tmp_Z=np.random.standard_normal(N)
            Z2=self.rol*Z1+np.sqrt(1-self.rol**2)*tmp_Z
            growthFactor1=drift1*np.exp(self.vol1*np.sqrt(dt)*Z1)
            growthFactor2=drift2*np.exp(self.vol2*np.sqrt(dt)*Z2)
            s1_path[0]=self.s1_0*growthFactor1[0]
            s2_path[0]=self.s2_0*growthFactor2[0]
            for i in range(1,N):
                s1_path[i]=s1_path[i-1]*growthFactor1[i]
                s2_path[i]=s2_path[i-1]*growthFactor2[i]
            geo_path=np.sqrt(s1_path*s2_path)
            arit_path=(s1_path+s2_path)/2.0
            arit_spath.append(arit_path[-1])
            geo_spath.append(geo_path[-1])
            del s1_path
            del s2_path
        if opt_type=='C':
            for i in range(self.path):
                arit_payoff=max(arit_spath[i]-self.K,0)
                arit_spath[i]=arit_payoff*np.exp(-self.r*self.T)
                geo_payoff=max(geo_spath[i]-self.K,0)
                geo_spath[i]=geo_payoff*np.exp(-self.r*self.T)
        else:
            for i in range(self.path):
                arit_payoff=max(-arit_spath[i]+self.K,0)
                arit_spath[i]=arit_payoff*np.exp(-self.r*self.T)
                geo_payoff=max(-geo_spath[i]+self.K,0)
                geo_spath[i]=geo_payoff*np.exp(-self.r*self.T)
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
        dt=0.01
        N=int(self.T/dt)
        drift1=np.exp((self.r-0.5*self.vol1**2)*dt)
        drift2=np.exp((self.r-0.5*self.vol1**2)*dt)
        if str.upper(self.type) == 'C':
            geo_c = np.exp(-self.r*self.T)*(self.bg0*np.exp(self.u_b*self.T)*norm.cdf(d1)-self.K*norm.cdf(d2))
            arit_spath,geo_spath,theta,confmc=self._cal(drift1,drift2,dt,N,self.type)
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
            geo_c = np.exp(-self.r*self.T)*(self.K*norm.cdf(-d2)-self.bg0*np.exp(self.u_b*self.T)*norm.cdf(-d1))
            arit_spath,geo_spath,theta,confmc=self._cal(drift1,drift2,dt,N,self.type)
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
