"""
A valid email address meets the following criteria:
- It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
- The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
- The domain and extension contain only English alphabetical characters.
- The extension is 1, 2, or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line. 

Hint: Try using Email.utils() to complete this challenge.
"""


import email.utils

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, email_addr = email.utils.parseaddr(s)
        if '@' in email_addr:
            domain, ext = email_addr.split('@')
            if ext.isalnum() and domain.isalnum():
                if 1 <= len(ext) <= 3:
                    return True
        return False
    except:
        return False

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