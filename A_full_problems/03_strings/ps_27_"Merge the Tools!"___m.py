"""
Consider the following:
- A string, s, of length n where s = C0,C1, ...Cn-1.
- An integer, k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k
characters in s. Then, use each ti to create string ui such that:

- The characters in ui are a subsequence of the characters in ti.
- Any repeat occurrence of a character is removed from the string such that each character in ui;
occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index
< j in ti, then do not include the character in string ui.

Given s and k, print n/k lines where each line i denotes string ui.

Function Description:
Complete the merge_the_tools function in the editor below.
The merge_the_tools function has the following parameters:
- string s: the string to analyze
- int k: the size of substrings to analyze

Prints:
Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format:
The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

Constraints:
- 1 <= n <= 10^4, where n is the length of s.
- 1 <= k <= n
- It is guaranteed that n is a multiple of k.
"""



def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        s = string[i:i+k]
        print(''.join(sorted(set(s), key=s.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)