"""
Task:\n You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.
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