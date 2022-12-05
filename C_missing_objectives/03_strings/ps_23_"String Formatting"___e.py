"""
Given an integer, n, print the following values for each integer from 1 to n:
"""


n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(i, end="")
    for j in range(1, i):
        print(j, end="")
    print()