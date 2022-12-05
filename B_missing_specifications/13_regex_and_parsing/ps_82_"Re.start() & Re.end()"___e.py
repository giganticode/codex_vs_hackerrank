"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
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