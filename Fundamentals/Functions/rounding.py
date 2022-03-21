def rounding(number):
    return round(number)


list_n = []
numbers = input().split(" ")
floater = map(float, numbers)
fl_list = list(floater)

for n in fl_list:
    r = rounding(n)
    list_n.append(r)

print(list_n)
