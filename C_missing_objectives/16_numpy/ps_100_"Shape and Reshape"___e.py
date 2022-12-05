"""
You are given a space separated list of nine integers. 
"""



import numpy as np

arr = np.array(list(map(int, input().split())))
arr.shape = (3, 3)
print(arr)