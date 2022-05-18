from collections import deque

kids = deque(input().split(' '))

tosses_count = int(input())

current = 0

while len(kids) > 1:
    current += 1
    kid = kids.popleft()
    if current < tosses_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current = 0

print(f'Last is {kids[0]}')
