"""
Input an integer n from STDIN. Then for all non-negative integers until n, print i * i.

Input Format:
The first and only line contains the integer, n.

Constraints:
1 <= n <= 20

Output Format:
Print n lines, one corresponding to each i.
"""




def main():
    n = int(input())
    for i in range(n):
        print(i * i)


if __name__ == '__main__':
    main()