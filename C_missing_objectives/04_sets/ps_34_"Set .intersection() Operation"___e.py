"""
The students of District College have subscriptions to English and French newspapers. 
"""



n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(len(n_set.intersection(b_set)))