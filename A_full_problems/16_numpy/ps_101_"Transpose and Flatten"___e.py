"""
You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format:
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format:
First, print the transpose array and then print the flatten.
"""


import numpy

n, m = map(int, input().split())

array = numpy.array([input().strip().split() for _ in range(n)], int)

print(array.transpose())
print(array.flatten())