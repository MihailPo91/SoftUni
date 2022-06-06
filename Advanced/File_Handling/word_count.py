import re


def read_words():
    with open('./words.txt') as file:
        return file.read().split()


def count_words_in_file(words):
    words_counts = {
        word: 0 for word in words
    }
    with open('./input.txt') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_counts[word] += words_in_line.count(word)
    return words_counts


words_to_find = read_words()
print(count_words_in_file(words_to_find))

