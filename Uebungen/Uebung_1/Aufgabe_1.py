import numpy as np


def algorithm1(p, q):
    right = np.sqrt((p ** 2) + q)
    return -p + right


def algorithm2(p, q):
    x1 = -p - np.sqrt((p ** 2) + q)
    return -q / x1


if __name__ == '__main__':
    ps = np.array([10 ** 2, 10 ** 4, 10 ** 6, 10 ** 7, 10 ** 8])
    q = 1
    for p in ps:
        print(f' x2 for q={q} and p={p}:')
        print(algorithm1(p, q))
        print(algorithm2(p, q))
        print()

print("=> Bei größer werdenden p ist algorithm2 genauer")

print('Da identischer Code bei Kommilitonen funktioniert habe ich meine hier "fehlerhafte" Implementation so gelassen. Funktioniert auf Linux, auf Windows nicht')
