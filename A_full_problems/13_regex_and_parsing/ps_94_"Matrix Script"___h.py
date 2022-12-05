"""
Neo has a complex matrix script. The matrix script is a N x M grid of strings. 
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format:
The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.
Note: A 0 score will be awarded for using 'if' conditions in your code.

Constraints:
0 < N,M < 100
Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format:
Print the decoded matrix script.
"""



import re

n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(input())

decoded = ''
for j in range(m):
    for i in range(n):
        decoded += matrix[i][j]

decoded = re.sub(r'(?<=[A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])', ' ', decoded)
print(decoded)