import re

text = input()
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(pattern, text)

threshold = 1
for char in text:
    if char.isdigit():
        threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)

    if coolness > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))