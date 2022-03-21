number_commands = int(input())
parking_database = {}

for line in range(number_commands):
    data = input().split(" ")
    command = data[0]

    if command == "register":
        name = data[1]
        license_number = data[2]
        if name not in parking_database:
            parking_database[name] = license_number
            print(f"{name} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")

    elif command == "unregister":
        name = data[1]
        if name in parking_database:
            del parking_database[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key in parking_database:
    print(f"{key} => {parking_database[key]}")
