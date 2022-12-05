"""
You are given a space separated list of {sixteen} integers. 
Your task is to convert this list into a {4X4} {list}.

Input Format:
A single line of input containing 16 space separated integers.

Output Format:
Print the {4X4} {list}.
"""

"""
SOLUTION
"""

l = list(map(int, input().split()))

print(l)

print(l[0:4])
print(l[4:8])
print(l[8:12])
print(l[12:16])