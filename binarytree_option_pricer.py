import math

import numpy as np
from scipy.stats import norm


class BinaryTree(object):

    def __init__(self, type, S0, K, T, sigma, r, q):
        """
        Parameters
        ----------
        type : {'eucall', 'euput', 'amcall', 'amput'}
        """
        self.type = type
        self.S0 = S0
        self.K = K
        self.T = T
        self.sigma = sigma
        self.r = r
        self.q = q

    # Black-Scholes
    def bs(self):

        if self.type == 'eucall':
            d1 = (math.log(self.S0 / self.K) + (self.r - self.q) * self.T) / (self.sigma * math.sqrt(self.T)) + 0.5 * self.sigma * math.sqrt(self.T)
            d2 = (math.log(self.S0 / self.K) + (self.r - self.q) * self.T) / (self.sigma * math.sqrt(self.T)) - 0.5 * self.sigma * math.sqrt(self.T)

            return self.S0 * math.exp(-self.q * self.T) * norm.cdf(d1) - self.K * math.exp(-self.r * self.T) * norm.cdf(d2)

        elif self.type == 'euput':
            d1 = (math.log(self.S0 / self.K) + (self.r - self.q) * self.T) / (self.sigma * math.sqrt(self.T)) + 0.5 * self.sigma * math.sqrt(self.T)
            d2 = (math.log(self.S0 / self.K) + (self.r - self.q) * self.T) / (self.sigma * math.sqrt(self.T)) - 0.5 * self.sigma * math.sqrt(self.T)

            return self.K * math.exp(-self.r * self.T) * norm.cdf(-d2) - self.S0 * math.exp(-self.q * self.T) * norm.cdf(-d1)

        else:
            raise ValueError('bad option type')

    # Binomial tree
    def bt(self, steps):

        u = math.exp(self.sigma * math.sqrt(self.T / steps))
        d = 1 / u
        p = (math.exp(self.r * (self.T / steps)) - d) / (u - d)

        tree = np.zeros([steps + 1, steps + 1])

        tree[0, 0] = self.S0

        # Forward pass
        for i in range(1, len(tree)):

            for j in range(i + 1):
                tree[j, i] = self.S0 * (u ** i) * (d ** (j * 2))

        # Inner pass
        for i in range(1, len(tree)):

            for j in range(i + 1):

                if 'call' in self.type:
                    tree[j, i] = max(tree[j, i] - self.K, 0)

                elif 'put' in self.type:
                    tree[j, i] = max(self.K - tree[j, i], 0)

                else:
                    raise ValueError('bad option type')

        # Backward pass
        if 'eu' in self.type:

            for i in range(steps - 1, -1, -1):

                for j in range(i + 1):
                    tree[j, i] = (p * tree[j, i + 1] + (1 - p) * tree[j + 1, i + 1]) * math.exp(-self.r * (self.T / steps))

        elif 'am' in self.type:

            for i in range(steps - 1, -1, -1):

                for j in range(i + 1):

                    if i == 0 and j == 0:
                        tree[j, i] = (p * tree[j, i + 1] + (1 - p) * tree[j + 1, i + 1]) * math.exp(-self.r * (self.T / steps))

                    else:
                        tree[j, i] = max(tree[j, i], (p * tree[j, i + 1] + (1 - p) * tree[j + 1, i + 1]) * math.exp(-self.r * (self.T / steps)))

        else:
            raise ValueError('bad option type')

        return tree[0, 0]

    #  Implied volatility
    @staticmethod
    def iv(type, S0, K, T, V, r, q, max_iter):
        """
        Parameters
        ----------
        type : {'eucall', 'euput', 'amcall', 'amput'}
        """
        if 'call' in type:
            sigma_est = math.sqrt(2 * abs((math.log(S0 / K) + (r - q) * T) / T))

            iter = 1

            while iter < max_iter:
                V_est = OptionPricer(type, S0, K, T, sigma_est, r, q).bsm()
                d1 = (math.log(S0 / K) + (r - q) * T) / (sigma_est * math.sqrt(T)) + 0.5 * sigma_est * math.sqrt(T)
                vega = S0 * math.exp(-q * T) * math.sqrt(T) * norm.pdf(d1)

                sigma_est -= (V_est - V) / vega

                iter += 1

            return sigma_est

        elif 'put' in type:
            sigma_est = math.sqrt(2 * abs((math.log(S0 / K) + (r - q) * T) / T))

            iter = 1

            while iter < max_iter:
                V_est = OptionPricer(type, S0, K, T, sigma_est, r, q).bsm()
                d1 = (math.log(S0 / K) + (r - q) * T) / (sigma_est * math.sqrt(T)) + 0.5 * sigma_est * math.sqrt(T)
                vega = S0 * math.exp(-q * T) * math.sqrt(T) * norm.pdf(d1)

                sigma_est -= (V_est - V) / vega

                iter += 1

            return sigma_est

        else:
            raise ValueError('bad option type')
