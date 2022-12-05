"""
A valid postal code P have to fullfil both below requirements:

P must be a number in the range from 100000 to 999999 inclusive.
P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. 
Where:
- regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
- regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

Input Format:
Locked stub code in the editor reads a single string denoting P from stdin and uses provided expression and your regular expressions to validate if P is a valid postal code.

Output Format
You are not responsible for printing anything to stdout. Locked stub code in the editor does that.
"""



regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)