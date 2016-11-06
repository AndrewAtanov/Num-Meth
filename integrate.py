import numpy as np


def integrate(x, y, method='rect'):
    if method in ['rect', 'trap']:
        return sum((y[:-1] + y[1:]) * (x[1:] - x[:-1]) / 2)
    elif method == 'simpson':
        return (sum(y[::2]) + sum(y[2:-2:2]) + 4 * sum(y[1:-1:2])) * (x[0] - x[1]) / 3
    else:
        ValueError('{} method not implemented!'.format(method))


def trap(x, y, dx=None):
    _agg = sum((y[:-1] + y[1:]) * (x[1:] - x[:-1]) / 2)
    _abs = np.abs((x[-1] - x[0]) ** 3 / 12 / x.shape[0]**2)
    return _agg, _abs


def simpson(h, y):
    if y.shape[0] % 2 != 1:
        raise ValueError('len of grid should be 2k+1 !')

    n = y.shape[0] - 1
    l = h * n
    _abs = np.abs(l * (h ** 4) / 2880.)
    return (sum(y[::2]) + sum(y[2:-2:2]) + 4 * sum(y[1:-1:2])) * h / 3, _abs
