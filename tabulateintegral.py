import numpy as np


class TabulateIntegral:
    def __init__(self):
        pass

    def read_ro(self):
        arr = np.load('ro.npz')
        ro, grid = arr['arr_1'], arr['arr_0']
        return  grid, ro

    def get_interpolation_coef(self):
        return np.random.randn(7)

    def tabulate_integral(self, grid):
        ro_grid, ro = self.read_ro()
        ans = []
        for y in grid:
            ans.append(self.compute_integral(ro, y))
        return np.array(ans)

    def write_coef(self):
        coef = self.get_interpolation_coef()
        np.savez('interpolation_coef.npz', coef)

    def compute_integral(self, ro, y):
        return 42
