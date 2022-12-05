"""
Task:\n You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.

Input Format:
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.

Output Format:
Print the desired value.
"""



import numpy as np

coef = np.array(input().split(), float)
x = float(input())
print(np.polyval(coef, x))