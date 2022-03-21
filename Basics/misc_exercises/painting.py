nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

nylon = int(input()) + 2
paint = int(input())
thinner = int(input())
hours = int(input())

added_paint = (paint * 0.10)
bags = 0.40

materials = nylon * nylon_price + (paint + added_paint) * paint_price + thinner * thinner_price + bags
work = materials * 0.30
work_price = hours * work

final_price = materials + work_price
print(final_price)