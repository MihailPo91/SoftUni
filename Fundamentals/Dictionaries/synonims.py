count = int(input())
dictionary = {}

for i in range(count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
