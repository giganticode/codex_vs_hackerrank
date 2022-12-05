"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5, or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""



import re

for _ in range(int(input())):
    s = input()
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', s) and not re.search(r'(\d)\1{3,}', s.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')