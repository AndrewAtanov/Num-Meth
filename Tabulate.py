import numpy as np

class Tabulate:
    def __init__(self):
        pass

    def make_tabulate(self, f, grid):
        return f(grid)

    def write_tab_func(self, f, grid, file):
        np.savez(file, grid, f)
