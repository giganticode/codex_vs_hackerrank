"""
ABC is a right triangle, 90 degree at B. 
"""


# Given the variables:
#   a - length of side AB
#   b - length of side BC
#   c - length of side AC
#
# Write a Python program that will print the area of the triangle using the above
# variables.
#
# Hint: Heron's formula
#
#   area = sqrt(s(s-a)(s-b)(s-c))
#
# where s = (a+b+c)/2

import math

a = 3
b = 4
c = 5

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)