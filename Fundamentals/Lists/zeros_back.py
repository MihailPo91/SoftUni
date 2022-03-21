number_string = input().split(", ")
zero_list = []

while "0" in number_string:
    number_string.remove("0")
    zero_list.insert(0, "0")

number_string.extend(zero_list)
int_number = (map(int, number_string))
print(list(int_number))


