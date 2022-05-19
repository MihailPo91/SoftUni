from collections import deque

green_light = int(input())
safe_window = int(input())

cars = deque()
cars_counter = 0
crashed = False

while True:
    command = input()

    if command == "END":
        break

    elif command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break

            if seconds_left == 0:
                cars_counter += 1
            if safe_window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                index = safe_window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[index]}.")
                crashed = True
                break

    else:
        cars.append(command)

if not crashed:
    print('Everyone is safe.')
    print(f'{cars_counter} total cars passed the crossroads.')

