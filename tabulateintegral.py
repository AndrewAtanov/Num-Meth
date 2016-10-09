import numpy as np


class TabulateIntegral:
    def __init__(self):
        pass

    def read_ro(self):
        arr = np.load('ro.npz')
        ro, grid = arr['arr_1'], arr['arr_0']

    def get_interpolation_coef(self):
        return np.random.randn(7)

    def compute_integral(self, grid):
        return np.sinc(grid)

    def write_coef(self):
        coef = self.get_interpolation_coef()
        np.savez('interpolation_coef.npz', coef)
