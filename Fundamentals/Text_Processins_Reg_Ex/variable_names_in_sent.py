import re

text = input()

matched = re.finditer(r"\b([_])([a-z-A-Z-0-9]+)\b", text)
output = []

for match in matched:
    output.append(match.group(2))

print(*output, sep=",")