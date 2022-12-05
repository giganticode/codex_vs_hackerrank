"""
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
"""



from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    for i in combinations_with_replacement(sorted(s), int(k)):
        print(''.join(i))