raw_key = input()

while True:
    line = input()
    if line == "Generate":
        break

    else:
        data = line.split(">>>")
        command = data[0]

        if command == "Contains":
            substring = data[1]
            if substring in raw_key:
                print(f"{raw_key} contains {substring}")
            else:
                print("Substring not found!")

        elif command == "Flip":
            direction = data[1]
            start_index = int(data[2])
            end_index = int(data[3])
            if direction == "Upper":
                target = raw_key[start_index:end_index]
                raw_key = raw_key.replace(target, target.upper())
                print(raw_key)
            elif direction == "Lower":
                target = raw_key[start_index:end_index]
                raw_key = raw_key.replace(target, target.lower())
                print(raw_key)

        elif command == "Slice":
            start_index = int(data[1])
            end_index = int(data[2])
            first = raw_key[:start_index]
            last = raw_key[end_index:]
            raw_key = first + last
            print(raw_key)

print(f"Your activation key is: {raw_key}")
