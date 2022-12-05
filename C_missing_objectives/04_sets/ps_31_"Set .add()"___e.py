"""
Rupal has a huge collection of country stamps. 
"""



n = int(input())

if n > 0 and n < 1000:
    stamps = set()
    for i in range(n):
        stamps.add(input())
    print(len(stamps))