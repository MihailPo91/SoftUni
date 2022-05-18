from collections import deque

number_of_pumps = int(input())

pumps = deque()

for _ in range(number_of_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(number_of_pumps):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
