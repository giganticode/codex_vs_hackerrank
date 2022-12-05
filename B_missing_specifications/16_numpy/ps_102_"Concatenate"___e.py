"""
Task:\n You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0.
"""



import numpy

n, m, p = map(int, input().split())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((a, b), axis=0))