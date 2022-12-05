"""
You are given an integer N followed by N email addresses. 
"""


import re

if __name__ == '__main__':
    N = int(input())
    emails = []
    for _ in range(N):
        emails.append(input())

valid = []
for email in emails:
    if re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email):
        valid.append(email)

valid.sort()
print(valid)