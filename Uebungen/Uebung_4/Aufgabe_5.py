import numpy as np


def getAj(M, j):
    if (j - 1) > 0:
        M1 = np.delete(M, 0, 0)
        M1 = np.delete(M1, 0, 1)
        return M1.copy()

    else:
        return M.copy()


def zerlegung(A):
    n = len(A)
    j = 1
    Hn = []

#R
    while (j < n):
        # 1)
        Aj = getAj(A, j)

        # 2)
        a1 = Aj[:, 0]
        a1[0] = a1[0] + np.sign(a1[0]) * np.linalg.norm(a1)  # v1

        # 3)
        fak = 2 / np.dot(a1, a1)
        H = a1.reshape(n- (j - 1), 1) * a1
        H = H * fak
        H = np.identity(n - (j - 1)) - H  # E - H

        # 4)
        if (len(H) == n):
            Mat = H
        else:
            Mat = np.identity(n)
            Mat[(n - len(H)):n, (n - len(H)):n] = H

        Hn.append(Mat)

        #5)
        A = Mat @ A

        j += 1


    R = A

    #Q
    Q = np.identity(n)
    for h in Hn:
         Q = Q * h
    Q.transpose()

    return Q, R


if __name__ == '__main__':
    A = np.array([[1, -5, -20], [-4, 11, -1], [8, -4, 2]])
    B = np.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]])

    Q, R = zerlegung(A)
    print('Q = ')
    print(Q)
    print('R = ')
    print(R)