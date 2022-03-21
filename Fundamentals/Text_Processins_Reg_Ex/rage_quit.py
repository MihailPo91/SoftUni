import re

input_string = input().upper()

split_input = re.split(r"(\d+)", input_string)
result_list = []

for i in range(0, len(split_input) - 1, 2):
    string_to_repeat = split_input[i]
    repeat_times = int(split_input[i + 1])
    result_list.append(string_to_repeat * repeat_times)

result_to_print = ''.join(result_list)
unique_characters = len(set(result_to_print))

print(f"Unique symbols used: {unique_characters}")
print(result_to_print)
