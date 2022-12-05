"""
Given an integer, n, print the following values for each integer from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
"""


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)