"""
You are given n scores. Store them in a list and find the score of the runner-up.
"""



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i] != arr[0]:
            print(arr[i])
            break