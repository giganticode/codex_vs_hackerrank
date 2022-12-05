"""
Task:\n You are given a 2-D array of size NxM.
Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None
"""


import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = np.array([input().split() for _ in range(n)], int)
    print(np.mean(arr, axis=1), np.var(arr, axis=0), np.std(arr), sep='\n')