text = input()

while text != "end":
    list_t = list(text)
    reversed_text = reversed(list_t)
    new_text = "".join(reversed_text)
    print(f"{text} = {new_text}")

    text = input()