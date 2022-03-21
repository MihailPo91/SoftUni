import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = re.finditer(pattern, text)

output = []

for match in matches:
    output.append(match.group())

print(*output, sep=" ")