"""
You are given a list of N lowercase English letters. 
"""


def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i]) != ord(chars[i+1]) - 1:
            return chr(ord(chars[i]) + 1)