"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""


from collections import deque

d = deque()

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()

print(*d)