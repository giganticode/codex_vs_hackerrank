"""
You are given N lines of CSS code. 
"""


import re

N = int(input())

for _ in range(N):
    line = input()
    print(re.sub(r'\s\s+', ' ', line))