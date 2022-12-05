"""
You are given N lines of CSS code. 
Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
"""


import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line = input()
        match = re.findall(r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', line)
        if match:
            print(*match, sep='\n')                