"""
You are given a text of N lines. The text contains -- and __ symbols.
Your task is to modify those symbols to the following:
-- → hyphens
__ → underscores
Both -- and __ should have a space " " on both sides.

Input Format:
The first line contains the integer, N.
The next N lines each contain a line of the text.
"""

import re

n = int(input())

for i in range(n):
    print(re.sub(r'(?<= )-( |$)', '-', re.sub(r'(?<= )__( |$)', '_', input())))