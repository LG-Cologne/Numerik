import numpy as np


def addRowFakTimes(A, row1, row2, fak):  # Matrix
    A[row1] = [a + fak * b for a, b in zip(A[row1], A[row2])]


def addCellFakTimes(b, cell1, cell2, fak):
    b[cell1] = b[cell1] + fak * b[cell2]


def addRowAndCellFakTimes(A, b, row1, row2, fak):
    addRowFakTimes(A, row1, row2, fak)
    addCellFakTimes(b, row1, row2, fak)


def makeSteppedForm(A, b):
    iter = 0
    n = len(A)

    while iter < n:
        pivot = A[iter, iter]  # Hauptdiagonale
        if pivot != 0:
            cur = iter + 1
            while cur < n:  # Werte unter Pivot
                if A[cur, iter] != 0:
                    fak = -(A[cur, iter] / pivot)
                    addRowAndCellFakTimes(A, b, cur, iter, fak)
                    # addRowFakTimes(A, cur, iter, -(A[cur][iter] / pivot))  # num + (-(num/pivot) * pivot)
                    # addCellFakTimes(b, cur, iter, -(A[cur][iter] / pivot))
                cur += 1

            iter += 1
        else:
            cur = iter + 1
            while cur < n:
                if A[cur, iter] != 0:
                    addRowAndCellFakTimes(A, b, iter, cur, 1)
                    # addRowFakTimes(A, iter, cur, 1)
                    # addCellFakTimes(b, iter, cur, 1)

                cur += 1


def solve(A, b):
    A = np.array(A, copy=True)

    makeSteppedForm(A, b)
    n = len(A)
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            b[i] -= A[i, j] * b[j]
        b[i] /= A[i, i]
    return b


if __name__ == '__main__':
    A = np.array([[1, 3, 1, 1], [0, 1, 0, 2], [2, 1, 0, 0], [0, 4, 4, 0]])
    b = np.array([6, 2, 4, 12])
    c = np.array([0, 1, 2, 3])

    solve(A, b)
    solve(A, c)

    print(A)
    print(b)
    print(c)
