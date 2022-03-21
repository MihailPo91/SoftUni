text = input()
result_text = ""

for ch in text:
    new_char = chr(ord(ch) + 3)
    result_text += new_char

print(result_text)