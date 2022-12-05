"""
There is a horizontal row of n cubes. 
The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print Yes if it is possible to stack the cubes. Otherwise, print No.
"""


#!/bin/python3
import sys

def left_or_right(cubes):
    left = cubes[0]
    right = cubes[-1]
    for i in range(1, len(cubes)):
        if cubes[i] < left:
            return False
        left = cubes[i]
    for i in range(len(cubes)-2, -1, -1):
        if cubes[i] < right:
            return False
        right = cubes[i]
    return True

def can_stack(cubes):
    if len(cubes) == 1:
        return True
    if left_or_right(cubes):
        return can_stack(cubes[1:-1])
    else:
        return False

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        sideLength = list(map(int, input().strip().split(' ')))
        if can_stack(sideLength):
            print("Yes")
        else:
            print("No")        