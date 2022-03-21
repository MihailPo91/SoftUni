def inventory(data):
    while True:
        command = input().split(" - ")

        if command[0] == "Craft!":
            break

        elif command[0] == "Collect":
            if command[1] not in data:
                data.append(command[1])
            else:
                pass

        elif command[0] == "Drop":
            if command[1] in data:
                data.remove(command[1])
            else:
                pass

        elif command[0] == "Combine Items":
            items = command[1].split(":")
            if items[0] in data:
                item_index = data.index(items[0])
                data.insert(item_index + 1, items[1])
            else:
                pass

        elif command[0] == "Renew":
            if command[1] in data:
                data.remove(command[1])
                data.append(command[1])

    return ", ".join(data)


journal = input().split(", ")
print(inventory(journal))
