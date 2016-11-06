import numpy as np
from scipy.integrate import trapz, simps, quad
from integrate import simpson, trap
import matplotlib.pylab as plt
import sys

experiments = [{
    'func': np.sin,
    'func_name': 'sin',
    'a': 0,
    'b': 3,
    'n': 11,
}, {
    'func': np.abs,
    'func_name': 'abs',
    'a': -1,
    'b': 1,
    'n': 11,
}, {
    'func': lambda x: np.sin(1/x),
    'func_name': 'sin(1/x)',
    'a': 0.01,
    'b': 2,
    'n': 111,
}]


for exp in experiments:
    print('{func_name} function:'.format(**exp))
    x = np.linspace(exp['a'], exp['b'], exp['n'])
    y = exp['func'](x)
    h = np.abs(x[1] - x[0])
    print('[{a}, {b}], h = {h}'.format(**exp, h=h))
    print('Scipy quad method {:.5f}'.format(quad(exp['func'], exp['a'], exp['b'])[0]))
    print()

    print('Trapezoidal rule:')
    print('My method {:.5f}'.format(trap(x, y)[0]))
    print('Scipy trapz method {:.5f}'.format(trapz(y, x)))
    print()

    print('Simpson rule:')
    print('My method {:.5f}'.format(simpson(h, y)[0]))
    print('Scipy simps method {:.5f}'.format(simps(y, x)))
    print('-------------------------------')


if len(sys.argv) >= 2 and sys.argv[1] == 'err-plot':
    a = -5
    b = 5
    func = lambda x: np.sin(x) ** 2
    real_area, _ = quad(func, a, b)

    errors = []
    t_errors = []
    n_grid = np.logspace(1, 3, dtype=int)
    for n in n_grid:
        x = np.linspace(a, b, n if n % 2 == 1 else n + 1)
        y = func(x)
        h = x[1] - x[0]
        # area, teor_err = trap(x, y)
        area, teor_err = simpson(h, y)
        # area = simps(y, dx=h)
        pract_err = np.abs(area - real_area)
        errors.append(pract_err)
        t_errors.append(teor_err)

    plt.plot(np.log(n_grid), np.log(errors), '--', label='Real errors')
    plt.plot(np.log(n_grid), np.log(t_errors), label='Theoretical errors')
    plt.title('$sin^2(x)$ function')
    plt.xlabel('log(n)')
    plt.ylabel('log(error)')
    plt.legend()
    plt.show()
