"""
You are given n scores. Store them in a list and find the score of the {third-place} score.

Input:
The first line contains n. 
The second line contains an array A[] of n integers each separated by a space.

Constraints:
2 <= n <= 10
-100 <= A[i] <= 100
"""

n = int(input())
scores = list(map(int, input().split()))
scores.sort()
print(scores[-3])