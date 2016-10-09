import numpy as np


def Ufunc(y):
    return np.sin(y)


def Sfunc(t):
    return np.cos(t)


def Zfunc(t):
    return np.log(t)


class DiffEq:
    def __init__(self):
        self.u = Ufunc
        self.z = Zfunc
        self.s = Sfunc
        self.x0 = None
        self.y0 = None
        self.beta = None
        self.T = None

    def set_parameters(self, x0, y0, beta, t):
        self.x0 = x0
        self.y0 = y0
        self.beta = beta
        self.T = t

    def read_parameters(self):
        pass

    def set_functions(self):
        pass

    def read_functions(self):
        pass

    def get_cauchy_solve(self):
        pass

    def write_solve(self):
        pass
