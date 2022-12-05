"""
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

Input Format:
A single line of input containing the string S.

Constraints:
0 < len(S) < 100

Output Format:
Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
"""



import re

S = input()

pattern = re.compile(r'([a-zA-Z0-9])\1+')
match = pattern.search(S)

print(match.group(1) if match else -1)