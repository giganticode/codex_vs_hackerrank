"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
"""



from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(input())):
        item, space, quantity = input().rpartition(' ')
        d[item] = d.get(item, 0) + int(quantity)
    for item, quantity in d.items():
        print(item, quantity)