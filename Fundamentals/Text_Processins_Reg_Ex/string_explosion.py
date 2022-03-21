text = input()
power = 0
output = ''

for i in range(len(text)):
    if text[i] != '>' and power > 0:
        power -= 1
    elif text[i] == '>':
        power += int(text[i+1])
        output += text[i]
    else:
        output += text[i]

print(output)
