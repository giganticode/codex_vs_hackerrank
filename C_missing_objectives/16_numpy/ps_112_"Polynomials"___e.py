"""
Task:\n You are given the coefficients of a polynomial P.
"""


import numpy as np

if __name__ == '__main__':
    n = int(input())
    x = np.array([float(i) for i in input().split()])
    y = np.array([float(i) for i in input().split()])
    p = np.poly1d(np.polyfit(x, y, n))
    print(np.around(p(80), decimals=3))