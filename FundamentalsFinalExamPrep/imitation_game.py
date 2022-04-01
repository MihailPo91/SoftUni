message = input()

while True:
    line = input()

    if line == "Decode":
        break

    else:
        line_split = line.split("|")
        command = line_split[0]

        if command == "Move":
            number_to_move = int(line_split[1])
            move = message[:number_to_move]
            whats_left = message[number_to_move:]
            message = whats_left + move

        elif command == "Insert":
            index = int(line_split[1])
            element = line_split[2]
            first_half = message[:index]
            second_half = message[index:]
            message = first_half + element + second_half

        elif command == "ChangeAll":
            sub_string = line_split[1]
            replacement = line_split[2]
            message = message.replace(sub_string, replacement)


print(f"The decrypted message is: {message} ")
