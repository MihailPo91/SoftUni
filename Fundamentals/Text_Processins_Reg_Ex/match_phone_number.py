import re
text = input()
matches = re.findall(r"\+359[ -]2[ -]\d{3}[ -]\d{4}\b", text)
print(", ".join(matches))