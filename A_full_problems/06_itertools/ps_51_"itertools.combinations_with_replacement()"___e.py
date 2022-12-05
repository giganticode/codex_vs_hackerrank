"""
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format:
A single line containing the string S and integer value k separated by a space.

Constraints:
0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format:
Print the combinations with their replacements of string S on separate lines.
"""



from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    for i in combinations_with_replacement(sorted(s), int(k)):
        print(''.join(i))