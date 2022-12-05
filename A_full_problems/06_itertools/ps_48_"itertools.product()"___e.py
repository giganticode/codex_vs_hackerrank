"""
You are given a two lists A and B. 
Your task is to compute their cartesian product AxB.

Input Format:
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

Constraints:
0 < A < 30
0 < B < 30

Output Format:
Output the space separated tuples of the cartesian product.
"""



from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))