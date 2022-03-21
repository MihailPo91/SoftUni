import re

pattern = r"(^|(?<=\s))([a-zA-Z0-9]+[\.|\-|\_]?[a-zA-Z-0-9]+)@([a-zA-Z]+[\-]?)([\.]?)[A-Za-z]+\.[A-Za-z]+\.?[A-Za-z]+\b"

text = input()

matched = re.finditer(pattern, text)

output = [match.group() for match in matched]

print(*output, sep="\n")