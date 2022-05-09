import numpy.linalg as lin
import numpy as np


def qr(a):
    return lin.qr(a)


if __name__ == '__main__':

    for n in range(5, 10, 20):
        a = np.zeros((n, n))
        np.fill_diagonal(a, 2)

        helper = [-1] * (n - 1)
        a += np.diagflat(helper, 1)
        a += np.diagflat(helper, -1)
        print(a)

