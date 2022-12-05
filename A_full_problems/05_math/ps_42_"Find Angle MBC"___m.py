"""
ABC is a right triangle, 90 degree at B. 
Therefore, angle ABC = 90 degree.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees.

Input Format:
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints: 
- 0 < AB <= 100
- 0 < BC <= 100 
- Lengths AB and BC are natural numbers.

Output Format:
Output angle MBC in degrees.
Note: Round the angle to the nearest integer.
"""



import math
ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan2(ab, bc)))))+ u'\N{DEGREE SIGN}')