import numpy as np


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n

    _sum = 0
    for i in range(1, n):
        _sum += f(a + i * h)

    return (h / 2) * (f(a) + 2 * _sum + f(b))


def trapezoidal_rule_vektor(f, a, b, n):
    h = (b - a) / n

    base = np.arange(1, n) * h + a
    base = f(base)

    return (h / 2) * (f(a) + 2 * np.sum(base) + f(b))


if __name__ == '__main__':
    ns = np.array([10, 50, 100, 500, 1000, 5000])
    a = 1/10
    b = 10
    def f(x): return 1 / x**2

    print(f'Integral of 1/x^2 from {a} to {b}:')
    for n in ns:
        print('n =', n)
        print('Old trapezoidal rule        :', trapezoidal_rule(f, a, b, n))
        print('Trapezoidal rule with vector:', trapezoidal_rule_vektor(f, a, b, n))
        print()