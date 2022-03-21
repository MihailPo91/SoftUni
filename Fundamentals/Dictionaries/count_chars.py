text = list(input())
dictionary = {}

for ch in text:
    if ch not in dictionary:
        if ch == " ":
            pass
        else:
            dictionary[ch] = 1
    elif ch in dictionary:
        dictionary[ch] += 1

for key in dictionary:
    print(f"{key} -> {dictionary[key]}")
