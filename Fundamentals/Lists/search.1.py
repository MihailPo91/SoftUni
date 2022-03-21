n = int(input())
search_word = input()
strings = list()
filtered = list()

for i in range(n):
    current_word = input()
    strings.append(current_word)
    if search_word in current_word:
        filtered.append(current_word)

print(strings)
print(filtered)