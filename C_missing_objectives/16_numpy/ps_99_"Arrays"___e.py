"""
You are given a space separated list of numbers.
"""


numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(sum(numbers))