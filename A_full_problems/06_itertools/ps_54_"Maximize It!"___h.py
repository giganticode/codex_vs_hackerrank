"""
You are given a function f(X)=X^2. You are also given K lists. The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S=(f(X1)+f(X2)+...+f(Xk))%M

Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format:
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

Constraints: 
1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 <= Magnitude of elements in list <= 10^9

Output Format:
Output a single integer denoting the value Smax.
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))