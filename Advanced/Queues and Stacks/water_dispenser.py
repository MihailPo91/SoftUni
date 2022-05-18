from collections import deque

litres_water = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        queue.append(name)

while True:
    command = input()

    if command == "End":
        print(f"{litres_water} liters left")
        break

    elif "refill" in command:
        command = command.split()
        litres_water += int(command[1])

    else:
        litres = int(command)

        if litres <= litres_water:
            litres_water -= litres
            print(f"{queue.popleft()} got water")

        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
