"""
You are given a text of N lines. The text contains && and || symbols.
"""



import re

N = int(input())

for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))