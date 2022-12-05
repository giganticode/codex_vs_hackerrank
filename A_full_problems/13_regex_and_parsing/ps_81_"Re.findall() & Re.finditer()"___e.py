"""
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Input Format:
A single line of input containing string S.

Constraints:
0 < len(S) < 100

Output Format:
Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.
"""



import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])', input(), flags=re.I)
print('\n'.join(match or ['-1']))