"""
You are given a positive integer N. 
Print a numerical triangle of height N-1 like the one below:
1
22
333
4444
55555
......

Use only arithmetic operations, a single for loop and print statement.

Input Format:
A single line containing integer, N.

Constraints:
1 <= N <= 9

Output Format:
Print N-1 lines as explained above
"""



for i in range(1, int(input())):
    print((10 ** i // 9) * i)