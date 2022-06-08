with open('text.txt', 'r') as file:
    for i, line in enumerate(file):
        reversed_words = []
        if i % 2 == 0:
            for ch in line:
                if ch in ',.-?!':
                    line = line.replace(ch, '@')
            words = line.split()
            for el in range(len(words)-1, -1, -1):
                reversed_words.append(words[el])

            print(*reversed_words, end=" ")
            print()

