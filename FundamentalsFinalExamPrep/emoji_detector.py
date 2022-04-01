import re

text = input()
pattern = r"([*|:]{2})([A-Z][a-z]{2,})(\1)"
matches = re.findall(pattern, text)

threshold = 1
for ch in text:
    if ch.isdigit():
        threshold *= int(ch)

cool_emojis = []
for emoji in matches:
    power = 0
    for ch in emoji[1]:
        power += ord(ch)
    if power > threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {threshold}")
if len(matches) > 0:
    print(f"{len(matches)} emojis found in the text. The cool ones are:")
    for emoji in cool_emojis:
        print(''.join(emoji))
