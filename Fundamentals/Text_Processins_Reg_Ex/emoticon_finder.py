text = input()

for n, ch in enumerate(text):
    if ch == ":":
        print(text[n] + text[n+1])