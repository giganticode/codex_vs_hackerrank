"""
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type {int}.

Input Format:
A single line of input containing space separated numbers.

Output Format:
Print the reverse NumPy array with type {int}.
"""

import numpy

def arrays(arr):
    return numpy.array(arr[::-1], dtype=int)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)