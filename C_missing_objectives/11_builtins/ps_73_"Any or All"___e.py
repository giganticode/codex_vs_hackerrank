"""
Task:\n You are given a space separated list of integers. 
"""



n = int(input())
arr = input().split()

if all(int(i)>=0 for i in arr):
    if any(i==i[::-1] for i in arr):
        print(True)
    else:
        print(False)
else:
    print(False)