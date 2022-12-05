"""
Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input Format:
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Constraints:
0 < N < 1000
Check whether N is greater than 0 and less than 1000.

Output Format:
Output the total number of distinct country stamps on a single line.
"""



n = int(input())

if n > 0 and n < 1000:
    stamps = set()
    for i in range(n):
        stamps.add(input())
    print(len(stamps))