"""
Task:\n You are given two arrays: A and B.
"""


import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = np.array([input().split() for _ in range(n)], int)
    b = np.array([input().split() for _ in range(n)], int)
    print(np.add(a, b))
    print(np.subtract(a, b))
    print(np.multiply(a, b))
    print(a // b)
    print(np.mod(a, b))
    print(np.power(a, b))