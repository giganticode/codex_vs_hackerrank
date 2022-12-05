"""
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format:
A single line containing the space-separated integers.

Constraints:
1 <= each integer <= 3

Output Format:
First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
"""


import numpy

if __name__ == '__main__':
    dim = tuple(map(int, input().split()))
    print(numpy.zeros(dim, dtype=numpy.int))
    print(numpy.ones(dim, dtype=numpy.int))