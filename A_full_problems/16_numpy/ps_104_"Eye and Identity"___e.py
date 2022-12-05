"""
Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.
Note: In order to get alignment correct, please insert the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format:
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

Output Format:
Print the desired NxM array.
"""



import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m, k=0))