#!/usr/bin/env python3
import numpy as np


def zerlegung(a):
    lu = np.array(a, copy=True, dtype=np.float32)
    n = len(lu)
    p = np.arange(n)

    for j in range(n - 1):
        if lu[j, j] == 0:
            for i in range(j + 1, n):
                if lu[i, j] != 0:
                    p[j] = i
                    lu[[j, i]] = lu[[i, j]]
                    break
        for i in range(j + 1, n):
            lu[i, j] /= lu[j, j]    #fak (+einsetzen)
            for i2 in range(j + 1, n):
                lu[i, i2] -= lu[i, j] * lu[j, i2]

    return lu, p


def find_first_and_swap(lu, n, p, j):
    for i2 in range(j + 1, n):
        if lu[i2, j] != 0:
            p[j] = i2
            lu[j], lu[i2] = lu[i2], lu[j]


def permutation(p, b):
    pb = np.array(b, copy=True, dtype=np.float32)
    for i, s in enumerate(p):
        pb[[i, s]] = pb[[s, i]]
    return pb


def vorwaerts(l, b):
    y = np.array(b, copy=True, dtype=np.float32)
    n = len(l)
    for i in range(1, n):
        for j in range(i):
            y[i] -= l[i, j] * y[j]
    return y


def rueckwaerts(u, y):
    x = np.array(y, copy=True, dtype=np.float32)
    n = len(u)
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            x[i] -= u[i, j] * x[j]
        x[i] /= u[i, i]
    return x


def solve(a, bs):
    xs = []
    lu, p = zerlegung(a)
    print('//////////////////////////////////////////')
    print(lu)
    print('//////////////////////////////////////////')
    for b in bs:
        pb = permutation(p, b)
        y = vorwaerts(lu, pb)
        xs.append(rueckwaerts(lu, y))
    return xs


if __name__ == '__main__':
    a = np.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]])
    print('A =')
    print(a)
    bs = [
        np.array([3, 5, 4, 5]),
        np.array([4, 10, 12, 11])
    ]
    xs = solve(a, bs)
    for b, x in zip(bs, xs):
        print('Lösung für b =', b)
        print('x =', x)

    print()
    print('----------------------------------------------------------------')
    print()

    for n in range(5, 25, 5):
        a = np.indices((n, n))
        a = 1 / (a[0] + a[1] + 1)
        b = 1 / np.arange(2, n + 2)
        x = solve(a, [b])[0]
        x_exact = np.zeros(n)
        x_exact[1] = 1
        print(f'A ({n}x{n}) =')
        print(a)
        print('b =', b)
        print('Lösung: x =', x)
        print('Exakte Lösung: x =', x_exact)
        print()
