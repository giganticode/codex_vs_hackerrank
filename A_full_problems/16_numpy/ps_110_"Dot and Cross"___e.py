"""
Task:\n You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.

Input Format:
The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format:
Print the matrix multiplication of A and B.
"""



import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))