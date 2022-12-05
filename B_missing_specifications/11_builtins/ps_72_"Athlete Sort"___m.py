"""
Task:\n You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. 

Note that K is indexed from 0 to M-1, where M is the number of attributes.
Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
"""



from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=itemgetter(k))

    for i in arr:
        print(*i)