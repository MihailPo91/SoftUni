words = input().split(" ")
words = list(map(lambda w: w.lower(), words))  # това може и после във фор цикъла
occurrences = {}    # lower_words = words.lower()

for word in words:
    if word not in occurrences:
        occurrences[word] = 0  # if not in ... occurrences[word] = 1
    occurrences[word] += 1  # else: occurrences += 1

for key, value in occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")
