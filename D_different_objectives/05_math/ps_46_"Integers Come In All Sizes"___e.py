"""
Read four numbers, a, b, c, and d, and print the result of (a^b + c{*}d).

Input Format:
Integers a, b, c, and d are given on four separate lines, respectively.

Constraints:
- 1 <= a <= 1000
- 1 <= b <= 1000
- 1 <= c <= 1000
- 1 <= d <= 1000
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)