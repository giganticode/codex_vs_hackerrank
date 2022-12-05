"""
Task:\n You are given a 2-D array of size NxM.
Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None

Input Format:
The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format:
First, print the mean.
Second, print the var.
Third, print the std.

Round the std output to 11 decimal places.
"""



import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))