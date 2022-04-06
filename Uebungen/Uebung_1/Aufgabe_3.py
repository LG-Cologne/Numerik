import numpy as np
import scipy.integrate as integ


def rectangleRight(f, a, b, n):
    h = (b - a) / n
    _sum = 0

    for i in range(n):
        _sum += f(a + i * h)

    return h * _sum


def rectangleLeft(f, a, b, n):
    h = (b - a) / n
    _sum = 0

    for i in range(1, n + 1):
        _sum += f(a + i * h)

    return h * _sum


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n

    _sum = 0
    for i in range(1, n):
        _sum += f(a + i * h)

    return (h/2) * (f(a) + 2 *_sum + f(b))

if __name__ == '__main__':
    ns = np.array([10, 50, 100, 500, 1000, 5000])

    a = 1 / 10
    b = 10


    def f(x):
        return 1 / x ** 2


    for n in ns:
        print(f'example 1: a={a}, b={b}, f=1/x^2 with n={n}')
        print('Left rectangles :', rectangleLeft(f, a, b, n))
        print('Right rectangles:', rectangleRight(f, a, b, n))
        print('Trapezoidal rule:', trapezoidal_rule(f, a, b, n))
        print('Exact solution  :', integ.quad(f, a, b)[0])
        print()

    print('-------------------------------------------')
    print()

    a = 1
    b = 2


    def f(x):
        return np.log(x)


    for n in ns:
        print(f'example 2: a={a}, b={b}, f=ln(x) with n={n}')
        print('Left rectangles :', rectangleLeft(f, a, b, n))
        print('Right rectangles:', rectangleRight(f, a, b, n))
        print('Trapezoidal rule:', trapezoidal_rule(f, a, b, n))
        print('Exact solution:  ', integ.quad(f, a, b)[0])
        print()