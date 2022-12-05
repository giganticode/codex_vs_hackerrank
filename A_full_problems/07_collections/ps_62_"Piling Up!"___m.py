"""
There is a horizontal row of n cubes. 
The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print Yes if it is possible to stack the cubes. Otherwise, print No.

Input Format:
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints
1 <= T <= 5
1 <= n <= 10^5
1 <= sideLength < 2^31


Output Format:
For each test case, output a single line containing either Yes or No.
"""



from collections import deque

def isPossible(arr):
    arr = deque(arr)
    while len(arr) > 1:
        if arr[0] >= arr[-1]:
            if arr[0] < arr[1]:
                return "No"
            else:
                arr.popleft()
        else:
            if arr[-1] < arr[-2]:
                return "No"
            else:
                arr.pop()
    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(isPossible(arr))