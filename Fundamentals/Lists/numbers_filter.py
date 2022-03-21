n = int(input())

numbers_list = list()

for i in range(n):
    current = int(input())
    numbers_list.append(current)

filter_word = input()
filtered = list()

for current_number in numbers_list:
    if filter_word == "even":
        if current_number % 2 == 0:
            filtered.append(current_number)
    if filter_word == "odd":
        if current_number % 2 != 0:
            filtered.append(current_number)
    if filter_word == "positive":
        if current_number >= 0:
            filtered.append(current_number)
    if filter_word == "negative":
        if current_number < 0:
            filtered.append(current_number)

print(filtered)



