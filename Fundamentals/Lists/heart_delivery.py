def heart_delivery(data):
    current_index_position = 0
    cupids_last_position = 0
    failed_houses = 0

    while True:
        command = input().split(" ")
        if command[0] == "Love!":
            break

        index = int(command[1]) + current_index_position
        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] <= 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")

        cupids_last_postion = index
        current_index_position = index

    for h in data:
        if h != 0:
            failed_houses += 1

    print(f"Cupid's last position was {cupids_last_position}.")
    if data.count(0) == len(user_input):
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {failed_houses} places.")


user_input = list(map(int, input().split("@")))
heart_delivery(user_input)





