"""
You are given two sets, A and B.
Your job is to find whether set {B} is a subset of set {A}.

If set {B} is subset of set {A}, print True.
If set {B} is not a subset of set {A}, print False.

Input Format:
The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Constraints:
- 0 < T < 21
- 0 < Number of elements in each set < 1001

Output Format:
Output True or False for each test case on separate lines.
"""

for _ in range(int(input())):
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
    print(a.issubset(b))
