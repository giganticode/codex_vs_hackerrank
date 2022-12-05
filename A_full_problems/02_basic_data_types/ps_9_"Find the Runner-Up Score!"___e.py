"""
You are given n scores. Store them in a list and find the score of the runner-up.

Input:
The first line contains n. 
The second line contains an array A[] of n integers each separated by a space.

Constraints:
2 <= n <= 10
-100 <= A[i] <= 100
"""




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] != arr[0]:
            print(arr[i])
            break