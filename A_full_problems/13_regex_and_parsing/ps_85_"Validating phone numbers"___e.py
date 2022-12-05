"""
Task:\n You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8 or 9.

Input Format:
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Constraints:
1 <= N <= 10
2 <= len(Number) <= 15

Output Format:
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. 
Do not print the quotes.
"""



import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = input()
        if re.match(r'[789]\d{9}$', number):
            print('YES')
        else:
            print('NO')