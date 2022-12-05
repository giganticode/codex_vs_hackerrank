"""
You are given two values a and b.
Perform integer division and print a/b.

Input Format:
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.

Constraints:
0 < T < 10

Output Format:
Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)