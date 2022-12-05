"""
Task:\n You are given a 2-D array with dimensions NXM.
Your task is to perform the {product} tool over axis 0 and then find the {sum} of that result.

Input Format:
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format:
Compute the {product} along axis 0. Then, print the {sum} of that {product}.
"""

import numpy

n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(array, axis=0)))