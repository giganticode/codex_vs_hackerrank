"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format:
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
"""



m = int(input())
m_arr = set(map(int, input().split()))
n = int(input())
n_arr = set(map(int, input().split()))

diff = m_arr.difference(n_arr)
diff.update(n_arr.difference(m_arr))

for i in sorted(diff):
    print(i)