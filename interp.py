import numpy as np


def cubic_spline(f, tau, m0=0, mN=0):
    if isinstance(tau, float):
        tau = np.array(tau * (f.shape[0] - 1))

    a, b = [], []


