import re

text = input()
searched_word = input()

matched = re.findall(r"\b" + searched_word + r"\b", text, re.IGNORECASE)

print(len(matched))