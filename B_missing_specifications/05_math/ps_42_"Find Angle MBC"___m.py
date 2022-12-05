"""
ABC is a right triangle, 90 degree at B. 
Therefore, angle ABC = 90 degree.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees.
"""



import math
ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan2(ab, bc)))))+ u'\N{DEGREE SIGN}')