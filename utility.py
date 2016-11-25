from numpy.polynomial.polynomial import polyval
import numpy as np


class PolyFunc:
    def __init__(self, coef):
        self.coef = coef

    def __call__(self, t):
        return polyval(t, self.coef)


class CubicSplineFunc:
    def __init__(self, m, t, a, b):
        self.m = m
        self.tau = t[1:] - t[:-1]
        self.t = t
        self.a = a
        self.b = b

    def _get_interval(self, t):
        if t < self.t[0] or t > self.t[-1]:
            raise ValueError('t should be from interpolated interval ({}, {})'.format(self.t[0], self.t[-1]))
        for i in range(len(self.t) - 1):
            if self.t[i] <= t <= self.t[i + 1]:
                return i

    def __call__(self, t):
        if isinstance(t, float):
            n = self._get_interval(t)
            return (self.m[n] * ((self.t[n+1] - t) ** 3) + self.m[n+1] * ((t - self.t[n]) ** 3)) / 6 / self.tau[n] \
                   + self.a[n] * t + self.b[n]
        else:
            ans = []
            for _t in t:
                ans.append(self(_t))

            return np.array(ans)
