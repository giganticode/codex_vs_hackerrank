"""
Given a full name, your task is to capitalize the name appropriately in Python3.
Create a solve function.

Input Format:
A single line of input containing the full name, S.

Constraints:
0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format:
Print the capitalized string, S.
"""




def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)