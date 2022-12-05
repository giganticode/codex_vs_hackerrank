"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""


if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    flag = True
    for i in range(n):
        B = set(map(int, input().split()))
        if not A.issubset(B):
            flag = False
            break
    print(flag)
