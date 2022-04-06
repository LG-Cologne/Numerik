import numpy as np


def gauss(a, b):
  return 'help'


def addRowFakTimes(A, row1, row2, fak):
    A[row1] = [a + fak * b for a, b in zip(A[row1], A[row2])]



def build_matrix(n):
    a = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a[i - 1, j - 1] = 1 / (i + j - 1)
    return a


def build_vector(n):
    b = np.zeros(n)
    for i in range(1, n + 1):
        b[i - 1] = 1 / (i + 1)
    return b


if __name__ == '__main__':
    b = np.array([1, 2, 3, 4])
    A = np.matrix([[1, 1, 1, 1],
                   [0, 1, 1, 1],
                   [0, 0, 1, 1],
                   [0, 0, 0, 1]])

    print(gauss(A, b))
