"""
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b.
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.

Input Format:
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format:
Print the result as described above.
"""



a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))