#!/usr/bin/env python3
#%%
import numpy as np
import sympy as sp
from sympy.abc import x


def get_gamma(ys, h):
    return 6 * (
        (ys[2:] - ys[1 : len(ys) - 1]) / h[1:]
        - (ys[1 : len(ys) - 1] - ys[: len(ys) - 2]) / h[: len(ys) - 2]
    )


def get_beta(a_diag, h, gamma):
    beta = np.zeros(len(a_diag) + 2)
    if len(a_diag) == 1:
        beta[1] = gamma[0] / a_diag[0]
    else:
        a_sec = np.array(h[1 : len(h) - 1], copy=True)
        for i in np.arange(1, len(a_diag) - 1):
            a_diag[i] = a_diag[i] / h[i] * a_diag[i - 1] - a_sec[i - 1]
            a_sec[i] = a_sec[i] / h[i] * a_diag[i - 1]
            gamma[i] = gamma[i] / h[i] * a_diag[i - 1] - gamma[i - 1]
        beta[-2] = (gamma[-1] / h[-2] * a_diag[-2] - gamma[-2]) / (a_diag[-1] / h[-2] * a_diag[-2] - a_sec[-1])
        for i in reversed(np.arange(len(a_diag) - 1)):
            beta[i + 1] = (gamma[i] - a_sec[i] * beta[i + 2]) / a_diag[i]
    return beta


def get_alpha(ys, h, beta):
    return (
        (ys[1:] - ys[: len(ys) - 1]) / h
        - 1 / 3 * beta[: len(beta) - 1] * h
        - 1 / 6 * beta[1:] * h
    )


# auswerten bzw. aufstellen der stückweisen Funktionen s3(x)
def get_s3s(xs, ys, h, alpha, beta):
    s3s = (
        ys[: len(ys) - 1]
        + alpha * (x - xs[: len(xs) - 1])
        + beta[: len(beta) - 1] / 2 * (x - xs[: len(xs) - 1]) ** 2
        + (beta[1:] - beta[: len(beta) - 1]) / (6 * h) * (x - xs[: len(xs) - 1]) ** 3
    )
    s3s_with_intervals = []
    for s3, xi1 in zip(s3s, xs[1:]):
        s3s_with_intervals.append((s3, x <= xi1))
    return s3s_with_intervals


def spline(ps):
    xs = ps[:, 0]
    ys = ps[:, 1]
    h = xs[1:] - xs[: len(xs) - 1]
    a_diag = 2 * (h[: len(h) - 1] + h[1:])
    gamma = get_gamma(ys, h)
    beta = get_beta(a_diag, h, gamma)
    alpha = get_alpha(ys, h, beta)
    return sp.Piecewise(*get_s3s(xs, ys, h, alpha, beta))


if __name__ == "__main__":
    f = 1 / (1 + x * x)

    f_func = sp.lambdify([x], f)
    for m in [3, 5, 7, 9, 11, 13]:
        ps = []
        for i in np.arange(m):
            xi = -5 + 10 / (m - 1) * i
            ps.append(xi)
            ps.append(f_func(xi))
        ps = np.array(ps).reshape(-1, 2)

        s = spline(ps)

        p_actual = sp.plot(f, (x, -5, 5), show=False)
        p_spline = sp.plot(s, (x, -5, 5), show=False)
        p_actual.append(p_spline[0])
        p_actual.show()
