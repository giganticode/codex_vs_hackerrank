"""
Task:\n You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)

Note: There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format:
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

Output Format:
Print the result of each operation in the given order under Task.
"""



import numpy

N, M = map(int, input().split())

A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A, B))
print(numpy.mod(A, B))
print(numpy.power(A, B))