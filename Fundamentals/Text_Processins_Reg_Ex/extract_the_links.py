import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

pattern = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))'

links = re.finditer(pattern, text)

for link in links:
    print(link.group())



