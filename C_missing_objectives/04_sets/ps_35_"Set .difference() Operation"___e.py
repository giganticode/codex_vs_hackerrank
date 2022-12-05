"""
Students of District College have a subscription to English and French newspapers. 
"""



n = int(input())

eng_sub = set(map(int, input().split()))

b = int(input())

french_sub = set(map(int, input().split()))

print(len(eng_sub.intersection(french_sub)))