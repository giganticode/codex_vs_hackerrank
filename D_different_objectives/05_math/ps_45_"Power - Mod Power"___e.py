"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of {gcd}(a,b{,m}). On the second line, print the result of {lcm}(a,b,{m}).

Input Format:
The first line contains a, the second line contains b, and the third line contains m.

Constraints:
1 <= a <= 10
1 <= b <= 10
2 <= m <= 1000
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input())
b = int(input())
m = int(input())

print(gcd(a, b))
print(lcm(a, b))
