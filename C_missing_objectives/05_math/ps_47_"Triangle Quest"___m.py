"""
You are given a positive integer N. 
"""


def solution(N):
    # write your code in Python 3.6
    pass
    bin_N = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    for i in bin_N:
        if i == '1':
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            current_gap += 1
    return max_gap