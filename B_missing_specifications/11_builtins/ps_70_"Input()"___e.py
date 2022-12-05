"""
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.
"""

x, k = int(input()), int(input())
print(k == eval(input()))
