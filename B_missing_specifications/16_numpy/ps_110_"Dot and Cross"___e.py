"""
Task:\n You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.
"""



import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))