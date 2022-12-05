"""
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the {product} of elements from set A.

Input Format:
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

Constraints:
0 < len(set(A)) < 100
0 < len(otherSets) < 1000
0 < N < 100

Output Format:
Output the {product} of elements in set A.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

len_set_a = int(input())
set_a = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    operation, len_other_set = input().split()
    other_set = set(map(int, input().split()))
    if operation == 'intersection_update':
        set_a.intersection_update(other_set)
    elif operation == 'update':
        set_a.update(other_set)
    elif operation == 'symmetric_difference_update':
        set_a.symmetric_difference_update(other_set)
    elif operation == 'difference_update':
        set_a.difference_update(other_set)

print(sum(set_a))