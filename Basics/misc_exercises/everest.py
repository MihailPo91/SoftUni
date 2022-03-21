days_counter = 1
climbed_already = 5364
everest = 8848
command = input()

while command != "END":
    meters_per_climb = int(input())

    if command == "Yes":
        days_counter += 1
        if days_counter > 5:
            print("Failed!")
            print(f"{climbed_already}")
            break
        climbed_already += meters_per_climb

    elif command == "No":
        climbed_already += meters_per_climb

    if climbed_already >= everest:
        print(f"Goal reached for {days_counter} days!")
        break

    command = input()

if command == "END":
    if climbed_already >= everest:
        print(f"Goal reached for {days_counter} days!")
    else:
        print("Failed!")
        print(f"{climbed_already}")

