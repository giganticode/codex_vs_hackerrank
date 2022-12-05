"""
Neo has a complex matrix script. The matrix script is a N x M grid of strings. 
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""


import re
import itertools

def decoding(s):
    return re.sub(r'\b[^a-zA-Z0-9]\b', ' ', ''.join([''.join(x) for x in zip(*[list(s[z::n]) for z,n in enumerate(reversed([len(list(g)) for k,g in itertools.groupby(s)]))])]))

print(decoding("S !e@t#c$h&o^l%r&d"))