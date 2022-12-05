"""
You are given a complex z. Your task is to convert it to polar coordinates.
"""


import cmath

z = complex(input())
r = abs(z)
phi = cmath.phase(z)

print(r)
print(phi)