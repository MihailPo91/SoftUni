def vowel_remover(user_input):
    vowels_list = ['a', 'o', 'u', 'e', 'i']
    new_list = [ch for ch in user_input if ch not in vowels_list]
    return "".join(new_list)


user_string = list(input().lower())
print(vowel_remover(user_string))

