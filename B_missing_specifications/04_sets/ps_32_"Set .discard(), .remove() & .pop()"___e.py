"""
Task:\n You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
"""


n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))