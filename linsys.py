import numpy as np


# def solve(a, b):
#     print('This meth')
#     if a.shape[0] != a.shape[1]:
#         raise ValueError('Matrix A should be quadratic.')
#
#     for col in range(a.shape[0]):
#         swap_idx = np.abs(a[col:, col]).argmax()
#         a[[col, swap_idx]] = a[[swap_idx, col]]
#         a[col] = a[col] / a[col, col]
#         print(a)
#         tmp = a[col].copy()
#         a -= a[:, col] * a
#         a[col] = tmp.copy()
#
#     return a


def solve(a, b):
    if a.shape[0] != a.shape[1]:
        raise ValueError('Matrix A should be quadratic.')

    p, q = [-a[0, 1] / a[0, 0]], [b[0] / a[0, 0]]

    for i in range(1, a.shape[0] - 1):
        tmp = p[-1]
        p.append(a[i, i + 1] / (-a[i, i] - a[i, i - 1] * p[-1]))
        q.append((a[i, i - 1] * q[-1] - b[i]) / (-a[i, i] - a[i, i - 1] * tmp))

    i = a.shape[0] - 1
    q.append((a[i, i - 1] * q[-1] - b[i]) / (-a[i, i] - a[i, i - 1] * p[-1]))
    x = [q[-1]]

    for i in range(a.shape[0] - 2, -1, -1):
        x.append(p[i] * x[-1] + q[i])

    return np.array(x[::-1])
