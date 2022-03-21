numbers_list = input().split(" ")

first_half = numbers_list[:(int(len(numbers_list) / 2))]
second_half = numbers_list[:(int(len(numbers_list) / 2)):-1]

sum_left = 0
for number in first_half:
    number = float(number)
    if number == 0:
        sum_left *= 0.8
    sum_left += number

sum_right = 0
for number in second_half:
    number = float(number)
    if number == 0:
        sum_right *= 0.8
    sum_right += number


if sum_left < sum_right:
    print(f"The winner is left with total time: {sum_left:.1f}")
else:
    print(f"The winner is right with total time: {sum_right:.1f}")