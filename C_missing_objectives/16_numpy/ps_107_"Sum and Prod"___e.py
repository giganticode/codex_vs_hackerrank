"""
Task:\n You are given a 2-D array with dimensions NXM.
"""


import numpy

n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(array, axis=0)))