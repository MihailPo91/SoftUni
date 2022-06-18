def words_sorting(*args):
    words = {}
    for word in args:
        words[word] = sum([ord(x) for x in word])

    if sum(words.values()) % 2 == 0:
        return '\n'.join([f"{key} - {value}" for key, value in sorted(words.items())])
    elif sum(words.values()) % 2 != 0:
        return '\n'.join([f"{key} - {value}" for key, value in sorted(words.items(), key=lambda x: x[1],reverse=True)])


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))