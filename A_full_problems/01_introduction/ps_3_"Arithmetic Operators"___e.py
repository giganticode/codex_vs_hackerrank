"""
Input two numbers a and b. Write python code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer, a.
The second line contains the second integer, b.

Constraints:
1 <= a <= 10^10
1 <= b <= 10^10

Output Format:
Print the three lines as explained above.
"""




def main():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


if __name__ == '__main__':
    main()