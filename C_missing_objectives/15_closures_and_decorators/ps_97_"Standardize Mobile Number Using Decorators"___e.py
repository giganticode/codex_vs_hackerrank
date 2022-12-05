"""
You are given N mobile numbers. 
"""


n = int(input())

for i in range(n):
    number = input()
    if number.startswith("7") or number.startswith("8") or number.startswith("9"):
        print("YES")
    else:
        print("NO")