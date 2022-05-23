import numpy as np


def get_dividierte_differenzen(val):
    length = len(val[0])

    x = val[0]
    y = val[1]

    d = np.zeros((length, length))

    for n in range(length):
        for m in reversed(range(length)):
            if n == m:
                d[n, m] = y[n]
            elif n > m:
                d[n, m] = d[n][m] = (d[n, m + 1] - d[n - 1, m]) / (x[n] - x[m])

    return d[:, 0]


def q(k, n, val, d, x):
    if k == 0:
        return d[n]
    else:
        return d[n - k] + (x - val[0, n - 1]) * q(k - 1, n, val, d, x)


def evalute(val, x):
    d = get_dividierte_differenzen(val)
    return q(len(val[0])-1, len(val[0])-1, val, d, x)



if __name__ == "__main__":
    values = np.array([[0, 1, 3], [3, 2, 6]])
    values_from_four = np.array([[-1, 0, 1, 3], [-2, 4, 6, 22]])

    print(get_dividierte_differenzen(values))

    print(evalute(values, 2))