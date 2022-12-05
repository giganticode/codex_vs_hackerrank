"""
You are given a string S. 
Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

Input Format:
A single line of input consisting of the string S.

Output Format:
A single line of output consisting of the modified string.

Constraints:
All the characters of S denote integers between 0 and 9.
1 <=| S |<= 10^4
"""



from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])