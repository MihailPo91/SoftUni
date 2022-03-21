gifts = input().split(" ")

command = input()
while command != "No Money":
    collectable = command.split(" ")
    command = collectable[0]
    gift = collectable[1]

    if command == "OutOfStock":
        for i, current_gift in enumerate(gifts):
            if current_gift == gift:
                gifts[i] = "None"

    elif command == "Required":
        index = int(collectable[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

    command = input()

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))






