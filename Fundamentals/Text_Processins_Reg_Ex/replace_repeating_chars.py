user_string = input()
current_char = ""
result = ""
for ch in user_string:
    if ch != current_char:
        current_char = ch
        result += current_char

print(result)