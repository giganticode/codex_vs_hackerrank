"""
Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
"""


n = int(input())

if n > 0 and n < 1000:
    stamps = set()
    for i in range(n):
        stamps.add(input())
    print(len(stamps))