"""
Task:\n You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
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