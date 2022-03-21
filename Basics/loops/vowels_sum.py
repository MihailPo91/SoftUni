word = input()
vowel_sum = 0

for letter in word:
    if letter == "a":
        vowel_sum += 1
    elif letter == "e":
        vowel_sum += 2
    elif letter == "i":
        vowel_sum += 3
    elif letter == "o":
        vowel_sum += 4
    elif letter == "u":
        vowel_sum += 5
print(vowel_sum)

