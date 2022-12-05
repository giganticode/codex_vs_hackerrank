"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
"""


def find_logo(name):
    name = name.lower()
    name = sorted(name)
    name = sorted(name, key=name.count, reverse=True)
    return name[:3]

print(find_logo("Nike"))