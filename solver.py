import numpy as np
from diffeq import DiffEq, PolyFunc
import Tabulate
from tabulateintegral import TabulateIntegral

def ro(x, a, b):
    return a * x * (b - x)


def _id(arg):
    return arg


def expr_funv(t, expr):
    try:
        return eval(expr)
    except:
        print('Error in eval')


class Solver:
    def __init__(self):
        self.ro = _id
        self.s = _id
        self.z = _id
        self.u = None

        self.diff = DiffEq()
        self.tab = TabulateIntegral()

        self.N = 50
        self.x0 = None
        self.y0 = None
        self.T = None

        self.x = None
        self.y = None

    def set_parameters(self, x0, y0, T):
        self.x0 = x0
        self.y0 = y0
        self.T = T
        self.diff.set_parameters(x0, y0, T)

    def write_tabular(self):
        pass

    def create_ro(self, a, b):
        def _r(x):
            return ro(x, a, b)

        self.ro = _r

    def create_s(self, expr):
        def f(t):
            return expr_funv(t, expr)

        self.s = f

    def create_z(self, expr):
        def f(t):
            return expr_funv(t, expr)

        self.z = f

    def Fi(self):
        return np.random.random()

    def choose_best_diffeq_solve(self, beta_grid):
        best_beta = 0
        best_fi = 1000
        best_x = None
        best_y = None
        for beta in beta_grid:
            x, y = self.diff.get_cauchy_solve(np.linspace(0, self.T, self.N), beta)
            if self.Fi() < best_fi:
                best_beta = beta
                best_x = x
                best_y = y
        return best_x, best_y, best_beta

    def t_grid(self):
        return np.linspace(0, self.T, self.N)

    def set_solve(self, x, y):
        self.x = x
        self.y = y

    def save_solve(self):
        np.savez('cauchy_solve.npz', self.t_grid(), self.x, self.y)

    def save_init_func(self):
        Tabulate.write_tab_func(self.ro, self.t_grid(), 'ro_tabulated.npz')
        Tabulate.write_tab_func(self.s, self.t_grid(), 's_tabulated.npz')
        Tabulate.write_tab_func(self.z, self.t_grid(), 'z_tabulated.npz')

    def tabulate_int(self):
        self.tab.read_ro()
        u_tab = self.tab.tabulate_integral(np.linspace(0, 10, self.N))
        self.tab.write_coef()
        self.u = PolyFunc(self.tab.coef)
