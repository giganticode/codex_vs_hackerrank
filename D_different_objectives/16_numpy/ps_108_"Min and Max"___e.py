"""
Task:\n You are given a 2-D array with dimensions NXM.
Your task is to perform the {max} function over axis 1 and then find the {min} of that.

Input Format:
The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format:
Compute the {max} along axis 1 and then print the {min} of that result.
"""

import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(a, axis=1)))