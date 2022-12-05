"""
Task:\n You are given a 1-D array, A. Your task is to print the floor, ceil, and rint of all the elements of A.

Note:
In order to get the correct output format, add the line numpy.set_printoptions(legacy='1.13') below the numpy import.
"""



import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(input().split(), float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))