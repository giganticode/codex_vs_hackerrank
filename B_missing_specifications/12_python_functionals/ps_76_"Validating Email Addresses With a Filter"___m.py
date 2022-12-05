"""
You are given an integer N followed by N email addresses. 
Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The extension can only contain letters.
The maximum length of the extension is 3.
"""



import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r'^[\w-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$', s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)