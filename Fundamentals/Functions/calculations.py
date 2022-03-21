def calculate(a, b, operator):

    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculate(first_num, second_num, input_operator))
