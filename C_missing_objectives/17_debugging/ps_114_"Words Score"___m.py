"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.
"""


import re

def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)

if __name__ == '__main__':
    print(binary_array_to_number([0,0,0,1]))
    print(binary_array_to_number([0,0,1,0]))