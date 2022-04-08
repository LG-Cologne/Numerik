import numpy as np


def addRowFakTimes(A, row1, row2, fak):  # Matrix
    A[row1] = [a + fak * b for a, b in zip(A[row1], A[row2])]


def zerlegung(a):
    # einmal durchlaufen und zeilen komplett tauchen. U geht dadurch nicht kaputt

    for iter in range(len(a)):
        if (a[iter][iter] == 0):
            for row in range(iter + 1, len(a)):
                if a[row][iter] != 0:
                    a[[iter, row]] = a[[row, iter]]
                    break

    for iter in range(len(a)):
        row = iter + 1
        while row < len(a):  # Werte unter Pivot
            cur = a[row, iter]
            pivot = a[iter][iter]

            if cur != 0:
                fak = -(cur / pivot)
                addRowFakTimes(a, row, iter, fak)
                a[row][iter] = fak

            row += 1
    return a


def permutation(p, b):
    y = 0
    return y


def vorwaerts(l, x):
    y = 0
    return y


def rueckwaerts(u, x):
    y = 0
    return y


if __name__ == '__main__':
    a = np.array([[0, 0, 0, 1],
                  [2, 1, 2, 0],
                  [4, 4, 0, 0],
                  [2, 3, 1, 0]])

    test = np.array([[1, 1, 1, 1],
                     [0, 1, 1, 1],
                     [0, 0, 1, 1],
                     [0, 0, 0, 1]])

    LU = zerlegung(test)
    print(LU)
