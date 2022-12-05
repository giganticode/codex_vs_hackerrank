"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
"""



from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    for i in range(1, int(k)+1):
        for j in combinations(sorted(s), i):
            print(''.join(j))