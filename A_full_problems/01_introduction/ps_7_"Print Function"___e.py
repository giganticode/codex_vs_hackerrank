"""
Input a positive integer n from STDIN. Without using any string methods, try to print the following:

123 ... n

Note that "..." represents the consecutive values in between.

Example:
n = 5
Print the string 12345.

Input Format:
The first line contains an integer n.

Constraints:
1 <= n <= 150

Output Format:
Print the list of integers from 1 through n as a string, without spaces.
"""



n = int(input())

for i in range(1, n+1):
    print(i, end="")