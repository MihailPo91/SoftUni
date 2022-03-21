def coordinates(coords):
    return min(coords)


x_list = []
y_list = []

number1, number2, number3, number4 = float(input()), float(input()), float(input()), float(input())
x_list.append(number1)
y_list.append(number2)
x_list.append(number3)
y_list.append(number4)

result_list = [coordinates(x_list), coordinates(y_list)]
print(tuple(list(map(int, result_list))))
