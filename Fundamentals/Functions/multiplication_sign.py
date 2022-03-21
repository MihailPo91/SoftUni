def multiplication_sign(numbers):
    positive_counter = 0
    for n in numbers:
        if n == 0:
            return "zero"
        elif n < 0:
            return "negative"
        else:
            positive_counter += 1
            if positive_counter == 3:
                return "positive"


num1, num2, num3 = int(input()), int(input()), int(input())
new_list = [num1, num2, num3]
print(multiplication_sign(new_list))
