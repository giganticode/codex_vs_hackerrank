"""
You are given a function f(X)=X^2. You are also given K lists. The ith list consists of Ni elements.
"""


def f(x):
    return x*x

def find_max_sum(arr, n, k):
    max_sum = 0
    for i in range(k):
        sum = 0
        for j in range(n):
            sum += f(arr[i][j])
        if sum > max_sum:
            max_sum = sum
    return max_sum

if __name__ == '__main__':
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    k = len(arr)
    n = len(arr[0])
    print(find_max_sum(arr, n, k))