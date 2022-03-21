def even(number):
    result = []
    for num in number:
        if int(num) % 2 == 0:
            result.append(int(num))
    return result


input_nums = input().split(" ")
print(even(input_nums))
