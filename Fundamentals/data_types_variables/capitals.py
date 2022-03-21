word = input()
list_word = []

for i in range(len(word)):
    if word[i].isupper():
        list_word.append(i)

print(list_word)
