"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z, & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""



import re

for _ in range(int(input())):
    s = input()
    print("Valid" if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}', r'([A-Z].*){2}', r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else "Invalid")