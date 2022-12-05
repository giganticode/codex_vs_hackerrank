"""
Task:\n You are given a 2-D array with dimensions NXM.
"""


import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = np.array([input().strip().split() for _ in range(n)], int)
    print(np.prod(np.sum(arr, axis=0)))