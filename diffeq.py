import numpy as np
from numpy.polynomial.polynomial import polyval
from utility import PolyFunc

def Ufunc(y):
    return np.sin(y)


def Sfunc(t):
    return np.cos(t)


def Zfunc(t):
    return np.log(t)


class DiffEq:
    def __init__(self):
        self.u = PolyFunc(np.random.randn(2))
        self.z = PolyFunc(np.random.randn(2))
        self.s = PolyFunc(np.random.randn(2))
        self.x0 = None
        self.y0 = None
        self.T = None

    def set_parameters(self, x0, y0, t):
        self.x0 = x0
        self.y0 = y0
        self.T = t

    def read_parameters(self):
        pass

    def set_functions(self):
        pass

    def read_functions(self):
        try:
            self.u = PolyFunc(np.load('u_coef.npz')['arr_0'])
            self.z = PolyFunc(np.load('z_coef.npz')['arr_0'])
            self.s = PolyFunc(np.load('s_coef.npz')['arr_0'])
        except FileNotFoundError:
            print('No file')

    def dxdt(self, t_grid):
        return t_grid ** 2

    def dydt(self, t_grid):
        return np.sin(t_grid)

    def get_cauchy_solve(self, t_grid, beta):
        x = [self.x0]
        y = [self.y0]
        dx = self.dxdt(t_grid)
        dy = self.dydt(t_grid)

        for i in range(1, t_grid.shape[0]):
            x.append(x[i - 1] + (t_grid[i] - t_grid[i-1]) * dx[i-1])
            y.append(y[i - 1] + (t_grid[i] - t_grid[i-1]) * dy[i-1])

        return np.array(x), np.array(y)
