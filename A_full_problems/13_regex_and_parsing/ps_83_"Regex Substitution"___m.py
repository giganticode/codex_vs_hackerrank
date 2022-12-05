"""
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format:
The first line contains the integer, N.
The next N lines each contain a line of the text.

Constraints
0 < N < 100
Neither && nor || occur in the start or end of each line.

Output Format:
Output the modified text.
"""



import re

N = int(input())

for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))