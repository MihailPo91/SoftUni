import re

text = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

output = []

for match in matches:
    output.append(match.group())

print(*output, sep=', ')