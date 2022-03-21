number_of_wagons = int(input())
train = [0 for n in range(number_of_wagons)]
command = [""]

while "End" not in command:
    command = input().split(" ")
    if "add" in command:
        train[-1] += int(command[1])
    elif "insert" in command:
        train[int(command[1])] += int(command[2])
    elif "leave" in command:
        train[int(command[1])] -= int(command[2])


print(train)