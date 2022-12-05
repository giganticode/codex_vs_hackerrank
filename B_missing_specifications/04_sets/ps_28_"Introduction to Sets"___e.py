"""
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Calculate the average of distinct values in array.
"""



def average(arr):
    return round(sum(set(arr))/len(set(arr)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)