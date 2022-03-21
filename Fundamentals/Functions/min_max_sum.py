def min_max_sum(number):
    print(f"The minimum number is {min(number)}")
    print(f"The maximum number is {max(number)}")
    print(f"The sum number is: {sum(number)}")


numbers = list(map(int, input().split(" ")))
min_max_sum(numbers)
