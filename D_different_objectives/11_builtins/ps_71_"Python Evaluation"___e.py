"""
You are given an expression in a line. Read that line as a string variable, such as var, and print {it sorted in reverse order}.

Constraint:
Input string is less than 100 characters.
"""

var = input()
print(sorted(var, reverse=True))