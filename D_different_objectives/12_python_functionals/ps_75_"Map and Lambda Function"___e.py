"""
You have to generate a list of the first N fibonacci numbers, 0 being the first number. 
Then, apply the map function and a lambda expression to {double and then square} each fibonacci number and print the list.

Input Format:
One line of input: an integer N.

Constraints:
0 <= N <= 15

Output Format:
A list on a single line containing the {doubled squares} of the first N fibonacci numbers.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
fib = [0, 1]

for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])

print(list(map(lambda x: x**2, map(lambda x: x*2, fib))))