import re

text = input()

pattern = r"([=/])(?P<destination>[A-Z][A-Za-z]{2,})\1"

destinations = re.finditer(pattern, text)

output = []

for d in destinations:
    output.append(d.group("destination"))

points = len("".join(output))
print(f"Destinations: {', '.join(output)}")
print(f"Travel Points: {points}")
