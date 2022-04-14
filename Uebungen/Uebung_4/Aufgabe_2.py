import numpy as np


def zerlegung(a):
    lu = np.array(a, copy=True, dtype=np.float32)
    p = np.arange(len(lu))

    for iter in range(len(lu)):
        highest = np.argmax(np.abs(lu[iter:, iter])) + iter

        p[iter] = highest
        lu[[iter, highest]] = lu[[highest, iter]]

        for row in range(iter + 1, len(lu)):  # Werte unter Pivot
            cur = lu[row, iter]
            pivot = lu[iter, iter]
            if cur != 0:
                fak = (cur / pivot)

                for col in range(iter + 1, len(lu)):
                    lu[row, col] = lu[row, col] + (-fak) * lu[iter, col]  # UpperMatrix

                lu[row, iter] = fak  # lowerMatrix

    return lu, p


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
