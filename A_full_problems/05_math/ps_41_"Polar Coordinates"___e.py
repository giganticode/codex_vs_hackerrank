"""
You are given a complex z. Your task is to convert it to polar coordinates.

Input Format:
A single line containing the complex number z. 
Note: complex() function can be used in python to convert the input as a complex number.

Constraints:
Given number is a valid complex number.

Output Format:
The first line should contain the value of r.
The second line should contain the value of phi.
"""



import cmath

z = complex(input())
r = abs(z)
phi = cmath.phase(z)

print(r)
print(phi)