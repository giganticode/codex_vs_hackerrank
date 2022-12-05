"""
Task:\n You are given a square matrix A with dimensions NXN. 
Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.
"""

import numpy

n = int(input())
a = numpy.array([list(map(float, input().split())) for _ in range(n)])
print(numpy.linalg.det(a))