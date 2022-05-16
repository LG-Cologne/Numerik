import numpy as np


def getHighest(a):
    highest = -1
    for row in range(n):
        for col in range(n):
            if abs(a[row, col]) > highest:
                highest = a[row, col]
                highestRow = row
                highestCol = col
    return (highestRow, highestCol)


def right_givens(A, c1, c2):
    givens = np.array([[c, s],
                       [-s, c]])
    A[:, [c1, c2]] = np.dot(A[:, [c1, c2]], givens)


def solve(a):
    isNitFeddisch = True
    while (isNitFeddisch):
        c1, c2 = getHighest(a)
        right_givens(a, c1, c2)

    return a

if __name__ == '__main__':

    for n in range(5, 10, 20):
        a = np.zeros((n, n))
        np.fill_diagonal(a, 2)

        helper = [-1] * (n - 1)
        a += np.diagflat(helper, 1)
        a += np.diagflat(helper, -1)
        print(a)
