"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""



from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    for i in list(permutations(s, k)):
        print(''.join(i))