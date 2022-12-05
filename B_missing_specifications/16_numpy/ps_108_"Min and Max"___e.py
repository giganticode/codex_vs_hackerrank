"""
Task:\n You are given a 2-D array with dimensions NXM.
Your task is to perform the min function over axis 1 and then find the max of that.
"""


import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(arr, axis=1)))