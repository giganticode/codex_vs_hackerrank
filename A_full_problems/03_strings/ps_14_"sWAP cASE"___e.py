"""
Input a string s and swap it's case. In other words, convert all lowercase letters to uppercase letters and vice versa.

Function Description:
Complete the swap_case function in the editor below.
The swap_case function has the following parameters:
- string s: the string to modify

Returns:
- string: the modified string

Input Format:
A single line containing a string s.

Constraints:
0 < len(s) <= 1000
"""




def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)