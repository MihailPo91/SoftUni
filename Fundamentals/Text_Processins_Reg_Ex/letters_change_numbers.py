alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
            "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
            "y": 25, "z": 26}

total_sum = 0
user_strings = input().split()

for string in user_strings:
    string_l = list(string)
    first = string_l[0]
    last = string_l[-1]
    if first.isupper():
        first = first.lower()
        total_sum += int(string[1:-1]) / alphabet[first]
    else:
        total_sum += int(string[1:-1]) * alphabet[first]

    if last.isupper():
        last = last.lower()
        total_sum -= alphabet[last]
    else:
        total_sum += alphabet[last]

print(f"{total_sum:.2f}")
