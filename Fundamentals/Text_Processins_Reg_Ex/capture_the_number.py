import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

matched = re.findall(r"\d+", text)
output = [match for match in matched]
print(*output, sep=" ")