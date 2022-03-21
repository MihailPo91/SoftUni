first_char_num = ord(input())
second_char_num = ord(input())

text_ords = list(map(ord, list(input())))
target_nums = []

for num in text_ords:
    if first_char_num < num < second_char_num:
        target_nums.append(num)

print(sum(target_nums))



