"""
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Calculate the average of distinct values in array.

Function Description:
Create an average function.

The average function has the following parameters:
int arr: an array of integers

Returns:
float: the resulting float value rounded to 3 places after the decimal

Input Format:
The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers, arr[i].

Constraints:
0 < N <= 100
"""



def average(arr):
    return round(sum(set(arr))/len(set(arr)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)