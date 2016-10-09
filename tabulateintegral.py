import numpy as np


class TabulateIntegral:
    def __init__(self):
        self.ro = None
        self.coef = None
        pass

    def read_ro(self):
        self.ro = np.load('ro_tabulated.npz')['arr_0']

    def get_interpolation_coef(self):
        return np.random.randn(7)

    def tabulate_integral(self, y_grid):
        ro = self.read_ro()
        ans = []
        for y in y_grid:
            ans.append(self.compute_integral(ro, y))
        return np.array(ans)

    def write_coef(self):
        self.coef = self.get_interpolation_coef()
        np.savez('interpolation_coef.npz', self.coef)

    def compute_integral(self, ro, y):
        return 42
