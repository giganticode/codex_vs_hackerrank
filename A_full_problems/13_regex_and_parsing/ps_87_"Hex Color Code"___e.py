"""
You are given N lines of CSS code. 
Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

Input Format:
The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Constraints:
0 < N < 50

Output Format:
Output the color codes with '#' symbols on separate lines.
"""



import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        match = re.findall(r'(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?:[;,.)]{1})', s)
        if match:
            for m in match:
                print(m)