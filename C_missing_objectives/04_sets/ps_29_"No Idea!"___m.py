"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
"""


def arrayIntersection(arr1, arr2, arr3):
    arr1.sort()
    arr2.sort()
    arr3.sort()
    i = j = k = 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return result

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(arrayIntersection(arr1, arr2, arr3))