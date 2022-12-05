"""
Task:\n You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
"""


import numpy as np

n = int(input())
coef = np.array(input().split(), float)
x = int(input())

print(np.polyval(coef, x))