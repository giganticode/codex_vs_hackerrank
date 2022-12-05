"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.

Function Description:
Complete the rangoli function in the editor below.
The rangoli function has the following parameters:
- int size: the size of the rangoli

Returns:
- string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format:
Only one line of input containing size, the size of the rangoli.

Constraints:
0 < size < 27
"""




def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)