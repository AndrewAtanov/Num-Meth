import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from utility import CubicSplineFunc
from interp import cubic_spline


start, end, N = -6, 6, 31
func = lambda x: np.sinc(x)

t = np.linspace(start, end, N)
f = func(t)

print(t, f)

scipy_cubic = interp1d(t, f, kind='cubic')

m, a, b = cubic_spline(f, t)

my_spline = CubicSplineFunc(m, t, a, b)

x = np.linspace(start, end, 100)
y = func(x)
plt.scatter(t, f)
plt.plot(x, scipy_cubic(x), label='scipy spline')
plt.plot(x, my_spline(x), label='my spline')
plt.plot(x, y, label='origin')
plt.legend()
plt.show()
