"""
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
"""


import re

S = input()

print(bool(re.search(r'^[0-9a-zA-Z\s+-]+$', S)))