"""
You are given a two lists A and B. 
"""


def solution(A, B):
    # write your code in Python 3.6
    pass
    if len(A) != len(B):
        return -1
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    if len(A) == 2:
        if A[0] > A[1]:
            return 1
        else:
            return 0
    if len(A) == 3:
        if A[0] > A[1]:
            if A[1] > A[2]:
                return 2
            else:
                return 1
        else:
            if A[0] > A[2]:
                return 1
            else:
                return 0
    if len(A) > 3:
        if A[0] > A[1]:
            if A[1] > A[2]:
                if A[2] > A[3]:
                    return 3
                else:
                    return 2
            else:
                if A[0] > A[3]:
                    return 2
                else:
                    return 1
        else:
            if A[0] > A[2]:
                if A[2] > A[3]:
                    return 2
                else:
                    return 1
            else:
                if A[0] > A[3]:
                    return 1
                else:
                    return 0