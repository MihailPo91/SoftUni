numbers = list(map(int, input().split(", ")))
maximum = max(numbers)
current_maximum = 10
last_maximum = 0

while len(numbers) > 0:
    temp_list = list()

    for n, number in enumerate(numbers):

        if last_maximum < number <= current_maximum:
            temp_list.append(number)
            numbers.remove(number)
            numbers.insert(n, 0)
        else:
            pass
    while 0 in numbers:
        numbers.remove(0)
    print(f"Group of {current_maximum}'s: {temp_list}")
    last_maximum = current_maximum
    current_maximum += 10

