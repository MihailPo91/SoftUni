def numbers_searching(*args):
    numbers = []
    duplicates = set()
    biggest_missing_number = None

    for num in args:
        if num not in numbers:
            numbers.append(num)
        else:
            duplicates.add(num)
    numbers = sorted(numbers)
    all_numbers = list(range(numbers[0], numbers[-1]))
    for n in all_numbers:
        if n not in numbers:
            biggest_missing_number = n

    return [biggest_missing_number, sorted(list(duplicates))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))