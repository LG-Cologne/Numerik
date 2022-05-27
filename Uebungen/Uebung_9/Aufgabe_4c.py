#!/usr/bin/env python3
#%%
import numpy as np
import sympy as sp
from sympy.abc import x


def get_a(xs, n):
    at = []
    for k in np.arange(n):
        at.append(xs ** k)
    return np.array(at).T


def cgls(a, b, x0):
    xk = x0
    sk = b - a @ xk
    pk = a.T @ sk
    rk = pk
    # und so weiter...


if __name__ == '__main__':
    xs = []
    for i in [1, 2, 3, 4, 5, 6, 7]:
        xi = 10 ** (i - 7)
        xs.append(xi)
    xs = np.array(xs)
    ys = xs + 1

    n = 5
    a = get_a(xs, n)
    x0 = np.zeros(n)
    ps = cgls(a, ys, x0)

    f = 0
    for i, p in enumerate(ps):
        f += p * x ** i

    p_plot = sp.plot(1 + x, (x, -5, 5), show=False)
    f_plot = sp.plot(f, (x, -5, 5), show=False)
    p_plot.append(f_plot[0])
    p_plot.show()
