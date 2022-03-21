budget = float(input())
kg_flour = float(input())

pack_eggs = kg_flour * 0.75
milk = (kg_flour + kg_flour * 0.25) / 4

price_per_loaf = kg_flour + pack_eggs + milk
bread_price_so_far = 0
current_bread_count = 0
colored_eggs = 0

while (budget - bread_price_so_far) > price_per_loaf:
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)
    bread_price_so_far += price_per_loaf

money_left = abs(budget - bread_price_so_far)

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")