"""
Task:\n You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format:
The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.

Output Format:
First, print the inner product.
Second, print the outer product.
"""



import numpy as np

a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.inner(a, b))
print(np.outer(a, b))