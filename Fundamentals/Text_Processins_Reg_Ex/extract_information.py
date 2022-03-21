number = int(input())

for text in range(number):
    sentence = input()
    for i in range(len(sentence)):
        if sentence[i] == "@":
            first_i_name = i + 1
        if sentence[i] == "|":
            last_i_name = i
        if sentence[i] == "#":
            first_i_age = i + 1
        if sentence[i] == "*":
            last_i_age = i
    name = sentence[first_i_name:last_i_name]
    age = int(sentence[first_i_age:last_i_age])
    print(f"{name} is {age} years old.")
