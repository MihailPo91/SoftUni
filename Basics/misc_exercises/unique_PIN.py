first_max_num = int(input())
second_max_num = int(input())
third_max_num = int(input())

for num1 in range(2, first_max_num + 1, 2):
    for num2 in range(2, second_max_num + 1):
        for num3 in range(2, third_max_num + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f"{num1} {num2} {num3}")

