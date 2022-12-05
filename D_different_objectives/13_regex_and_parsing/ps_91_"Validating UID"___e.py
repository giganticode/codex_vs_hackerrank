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

Input Format:
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format:
For each test case, print 'OK' if the UID is valid. 
Otherwise, print 'NOT VALID UID', on separate lines. Do not print the quotation marks.
"""

import re

for _ in range(int(input())):
    s = input()
    if re.search(r'^[A-Z]{2}', s) and re.search(r'\d\d\d', s) and re.search(r'[A-Za-z0-9]{10}', s) and not re.search(r'(.)\1', s):
        print('Valid')
    else:
        print('Invalid')