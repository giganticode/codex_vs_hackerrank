"""
Task:\n You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is {an even} integer.

Input Format:
The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Constraints:
0 < N < 100

Output Format:
Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1
    for word in note:
        if word in magazine_dict:
            if magazine_dict[word] > 0:
                magazine_dict[word] -= 1
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)