import numpy as np
import math as m


def algorithm1(n, x):
    final = 0
    for k in range(n):
        final += x ** k / m.factorial(k)

    return final


def algorithm2(n, x):
    final = 0
    for k in range(n):
        final += x ** (n - k) / m.factorial(n - k)

    return final


if __name__ == '__main__':
    xs = np.array([2, 3, 5])
    ns = np.array([10, 20, 100])
    for x in xs:
        for n in ns:
            print(f' e for n={n} and x={x}:')
            print(algorithm1(n, x))
            print(algorithm2(n, x))
            print()
