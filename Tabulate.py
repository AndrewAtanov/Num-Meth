import numpy as np


def write_tab_func(f, grid, file):
    np.savez(file, grid, f(grid))
