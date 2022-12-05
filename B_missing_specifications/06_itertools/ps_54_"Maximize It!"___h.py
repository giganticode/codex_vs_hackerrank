"""
You are given a function f(X)=X^2. You are also given K lists. The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S=(f(X1)+f(X2)+...+f(Xk))%M

Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(results)