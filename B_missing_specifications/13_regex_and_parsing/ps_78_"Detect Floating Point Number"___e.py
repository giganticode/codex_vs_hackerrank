"""
You are given a string N.
Your task is to verify that N is a floating point number.
"""



import re

for _ in range(int(input())):
    print(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input()))