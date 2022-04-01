text = input()

line = input()
while line != "Travel":
    data = line.split(":")
    command = data[0]
    if command == "Add Stop":
        index = int(data[1])
        string_to_add = data[2]
        if 0 <= index < len(text):
            first_half = text[:index]
            second_half = text[index:]
            text = first_half + string_to_add + second_half
            print(text)

    elif command == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        first_part = text[:start_index]
        last_part = text[end_index+1:]
        if len(text) > start_index and len(text) > end_index:
            text = first_part + last_part
            print(text)
        else:
            print(text)
    elif command == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in text:
            text = text.replace(old_string, new_string)
            print(text)

    line = input()

print(f"Ready for world tour! Planned stops: {text}" )
