"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format:
The first line contains the string S.
The second line contains the string k.

Constraints
0 < len(S) < 100
0 < len(k) < len(S)

Output Format:
Print the tuple in this format: (start_index, end_index).
If no match is found, print (-1, -1).
"""



import re

if __name__ == '__main__':
    s = input()
    k = input()
    pattern = re.compile(k)
    m = pattern.search(s)
    if not m:
        print("(-1, -1)")
    while m:
        print("({0}, {1})".format(m.start(), m.end() - 1))
        m = pattern.search(s, m.start() + 1)