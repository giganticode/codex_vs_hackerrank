"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""



from collections import Counter

if __name__ == '__main__':
    X = int(input())
    sizes = Counter(map(int, input().split()))
    N = int(input())
    money = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if sizes[size]:
            money += price
            sizes[size] -= 1
    print(money)