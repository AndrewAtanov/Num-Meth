import numpy as np
from linsys import solve


def cubic_spline(f, t, m0=0, mN=0):
    tau = t[1:] - t[:-1]

    N = f.shape[0] - 1
    a = [[(tau[0] + tau[1]) / 3, tau[1] / 6, 0]]

    b = (f[2:] - f[1:-1]) / tau[1:] - (f[1:-1] - f[:-2]) / tau[:-1]

    for n in range(2, f.shape[0] - 2):
        a.append([tau[n-1] / 6, (tau[n-1] + tau[n]) / 3, tau[n] / 6])

    a.append([0, tau[N - 2]/6, (tau[N-2] + tau[N-1])/3])
    a = np.array(a)

    m = np.concatenate(([[m0], solve(a, b), [mN]]))

    a = (f[1:] - f[:-1]) / tau - (m[1:] - m[:-1]) * tau / 6
    b = f[:-1] - m[:-1] * tau**2 / 6 - a * t[:-1]

    return m, a, b
