string = input()

while True:
    line = input()
    if line == "Done":
        break
    else:
        data = line.split(" ")
        command = data[0]
        if command == "TakeOdd":
            new_string = [string[index] for index in range(len(string)) if index % 2 != 0]
            string = "".join(new_string)
            print(string)
        elif command == "Cut":
            index = int(data[1])
            length = int(data[2])
            first = string[:index]
            last = string[index+length:]
            string = first + last
            print(string)
        elif command == "Substitute":
            old = data[1]
            new = data[2]
            if old in string:
                string = string.replace(old, new)
                print(string)
            else:
                print("Nothing to replace!")

print(f"Your password is: {string}")

