"""
You are given a string s consisting only of digits 0-9, commas ,, and dots .
"""


def solution(s):
    s = s.replace(',', '.')
    s = s.split('.')
    s = [int(i) for i in s]
    return sum(s)