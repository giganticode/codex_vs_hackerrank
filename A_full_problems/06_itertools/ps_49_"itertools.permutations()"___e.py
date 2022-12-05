"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format:
A single line containing the space separated string S and the integer value k.

Constraints:
0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format:
Print the permutations of the string S on separate lines.
"""



from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    for i in list(permutations(s, k)):
        print(''.join(i))