user_input = input().split(", ")

for word in user_input:
    is_valid = True
    if 3 > len(word) or len(word) > 16:
        is_valid = False
    for ch in word:
        if not ch.isdigit() and not ch.isalpha() and ch != "-" and ch != "_":
            is_valid = False
        if " " in word:
            is_valid = False
    if is_valid:
        print(word)
