#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np


def gauss(a, b):
    a = np.array(a, copy=True)
    n = len(a)

    for column in range(n - 1):
        for row in range(column + 1, n):
            a[row, column] = a[row, column] / a[column, column]
            for column2 in range(column + 1, n):
                a[row, column2] -= a[row, column] * a[column, column2]

    for row in range(1, n):
        for column in range(row):
            b[row] -= a[row, column] * b[column]

    for row in reversed(range(n)):
        for column in range(row + 1, n):
            b[row] -= a[row, column] * b[column]
        b[row] /= a[row, row]

    return b


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
    A = np.array([[1, 3, 1, 1], [0, 1, 0, 2], [2, 1, 0, 0], [0, 4, 4, 0]])
    print(f'A = {A}')
    print()

    b1 = np.array([6, 2, 4, 12])
    print(f'For b1 = {b1}')
    print(f'Solution: {gauss(A, b1)}')
    print()

    b2 = np.array([8, 7, 1, 12])
    print(f'For b2 = {b2}')
    print(f'Solution: {gauss(A, b2)}')
    print()

    A = build_matrix(10)
    b = build_vector(10)
    print(f'A = {A}')
    print(f'For b = {b}')
    print(f'Solution: {gauss(A, b)}')