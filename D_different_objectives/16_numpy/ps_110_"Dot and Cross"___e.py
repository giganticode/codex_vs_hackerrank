"""
Task:\n You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute {the logical or operation on the arrays}.

Input Format:
The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format:
Print the {result of the operation}.
"""

import numpy

n = int(input())
a = numpy.array([list(map(int, input().split())) for _ in range(n)])
b = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.bitwise_or(a, b))