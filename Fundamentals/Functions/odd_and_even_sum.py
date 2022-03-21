def odd_even_sum(number):
    num_str = str(number)
    evens = 0
    odds = 0
    for n in range(len(num_str)):
        if int(num_str[n]) % 2 == 0:
            evens += int(num_str[n])
        elif int(num_str[n]) % 2 != 0:
            odds += int(num_str[n])
    print(f"Odd sum = {odds}, Even sum = {evens}")


input_number = int(input())

odd_even_sum(input_number)


