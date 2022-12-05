"""
Raghu is a shoe shop owner. His shop has X number of shoes.
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