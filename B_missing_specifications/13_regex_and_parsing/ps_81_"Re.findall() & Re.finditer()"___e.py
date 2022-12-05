"""
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
"""

import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])', input(), flags=re.I)
print('\n'.join(match or ['-1']))


import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])', input(), flags=re.I)
print('\n'.join(match or ['-1']))