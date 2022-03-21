phonebook = {}

command = input()

while len(command) > 1:
    command_explode = command.split("-")
    name = command_explode[0]
    number = command_explode[1]

    phonebook[name] = number
    command = input()

for i in range(int(command)):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
