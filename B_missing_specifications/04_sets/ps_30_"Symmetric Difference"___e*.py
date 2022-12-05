"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""


m = int(input())
m_arr = set(map(int, input().split()))
n = int(input())
n_arr = set(map(int, input().split()))

diff = m_arr.difference(n_arr)
diff.update(n_arr.difference(m_arr))

for i in sorted(diff):
    print(i)