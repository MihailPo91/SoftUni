numbers = input().split()
string = input()
string_list = list(string)
joined_string = "".join(string_list)
new_list = list(joined_string)
some_sum = 0

for number in numbers:
    new_number = list(number)
    for n in new_number:
        some_sum += int(n)
    if some_sum < len(string):
        index = some_sum
        print(new_list[int(index)], end="")
        if new_list[int(index)] in new_list:
            new_list.pop(int(index))
        string = "".join(new_list)
        some_sum = 0
    else:
        index = some_sum - len(string)
        print(new_list[int(index)], end="")
        if new_list[int(index)] in new_list:
            new_list.pop(int(index))
        string = "".join(new_list)
        some_sum = 0





