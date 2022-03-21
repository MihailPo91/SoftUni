def rope_take_skip(taken_list, skipped_list, main_list):
    result_list = []
    skip_l = []
    for take, skip in zip(taken_list, skipped_list):
        result_list.append(main_list[:take])
        del main_list[:take]
        skip_l.append(main_list[:skip])
        del main_list[:skip]
    joined = ""
    for list in result_list:
        joined += "".join(list)
    return joined


rope_string = input()
rope_list = list(rope_string)

digits = [i for i in rope_string if i.isdigit()]
non_digits = [i for i in rope_string if not i.isdigit()]

take_list = []
skip_list = []

for n, number in enumerate(digits):
    if n % 2 == 0:
        take_list.append(int(number))
    else:
        skip_list.append(int(number))


print("".join(rope_take_skip(take_list, skip_list, non_digits)))
