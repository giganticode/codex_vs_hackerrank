"""
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command, n = input().split()
    B = set(map(int, input().split()))
    getattr(A, command)(B)

print(sum(A))