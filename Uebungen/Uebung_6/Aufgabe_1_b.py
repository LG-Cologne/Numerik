import numpy as np


def mises(a, x, n):
    i = 0
    xSchlange = ([1, 1, 0])
    while (i <= n):
        xbefore = x
        x = a * x
        i = i + 1
        print("Iteration: " + i + "-> x= " + x)
    return np.dot(xSchlange, x) / np.dot(xSchlange, xbefore)


if __name__ == '__main__':
    a = ([[4, 2, 1],
          [2, 4, 2],
          [1, 2, 4]])

    x0 = ([1, 0, 0])

    print(mises(a, x0, 5))
