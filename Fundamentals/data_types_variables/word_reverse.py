word = input()
word_reverse = ""

for i in range(len(word)-1, -1, -1):
    word_reverse += word[i]
print(word_reverse)
