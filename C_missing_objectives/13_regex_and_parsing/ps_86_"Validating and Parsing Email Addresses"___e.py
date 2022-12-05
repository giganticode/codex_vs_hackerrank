"""
A valid email address meets the following criteria:
"""


import re

def is_valid_email(addr):
    if re.match(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', addr):
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')            