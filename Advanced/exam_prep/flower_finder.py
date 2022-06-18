from collections import deque

vowels = deque(input().split())
consonants = input().split()

is_found = False

flowers = {
    'rose': {
        'r': False,
        'o': False,
        's': False,
        'e': False
    },
    'tulip': {
        't': False,
        'u': False,
        'l': False,
        'i': False,
        'p': False
    },
    'lotus': {
        'l': False,
        'o': False,
        't': False,
        'u': False,
        's': False

    },
    'daffodil': {
        'd': False,
        'a': False,
        'f': False,
        'o': False,
        'i': False,
        'l': False
    }
}

while vowels and consonants:
    if is_found:
        break

    vowel = vowels.popleft()
    consonant = consonants.pop()
    for key, value in flowers.items():
        for char in value:
            if vowel == char:
                flowers[key][char] = True
            if consonant == char:
                flowers[key][char] = True
    for key, value in flowers.items():
        is_found = True
        for char in value:
            if flowers[key][char] is False:
                is_found = False
                break
        else:
            print(f'Word found: {key}')
            break


if is_found:
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')
else:
    print('Cannot find any word!')
    if vowels:
        print(f'Vowels left: {" ".join(vowels)}')
    if consonants:
        print(f'Consonants left: {" ".join(consonants)}')




