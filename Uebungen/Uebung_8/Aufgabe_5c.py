#%%
import numpy as np
from matplotlib import pyplot as plt
from sympy import symbols
from sympy.plotting import plot
from sympy.abc import x
import math

# Aus 5 a):
def get_dividierte_differenzen(val):
    length = len(val[0])

    x = val[0]
    y = val[1]

    d = np.zeros((length, length))

    for n in range(length):
        for m in reversed(range(length)):
            if n == m:
                d[n, m] = y[n]
            elif n > m:
                d[n, m] = d[n][m] = (d[n, m + 1] - d[n - 1, m]) / (x[n] - x[m])

    return d[:, 0]


def q(k, n, val, d):
    if k == 0:
        return d[n]
    else:
        return d[n - k] + (x - val[0, n - 1]) * q(k - 1, n, val, d)


def evalute(val):
    d = get_dividierte_differenzen(val)
    return q(len(val[0]) - 1, len(val[0]) - 1, val, d)


# 5 a) Ende


def f(x):
    return 1 / (1 + x**2)


p1 = plot(f(x), show=False)


m = (9,11,13)
for m_val in m:
    for i in np.arange(len(m)):
        x[i] = -5 * math.cos(math.pi(2 * i + 1) / (2 * m))
        y[i] = f(x[i])

    values = (x, y)
    plot = plot(evalute(values), show=False)
    p1.append(plot[0])

p1.show()
# %%

# %%
