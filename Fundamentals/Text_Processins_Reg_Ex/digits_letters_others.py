text = input()
digits = ""
letters = ""
other = ""

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch

print(digits)
print(letters)
print(other)