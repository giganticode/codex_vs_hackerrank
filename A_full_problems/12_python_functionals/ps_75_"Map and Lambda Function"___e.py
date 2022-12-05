"""
You have to generate a list of the first N fibonacci numbers, 0 being the first number. 
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Input Format:
One line of input: an integer N.

Constraints:
0 <= N <= 15

Output Format:
A list on a single line containing the cubes of the first N fibonacci numbers.
"""



cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))