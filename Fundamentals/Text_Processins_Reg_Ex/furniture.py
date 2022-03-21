import re
total_spent = 0
furniture = []
pattern = r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"

while True:
    text = input()
    if text == "Purchase":
        break

    result = re.match(pattern, text)
    if result is not None:
        product = result[1]
        price = float(result[2])
        quantity = float(result[3])
        total_spent += price * quantity
        furniture.append(product)


print("Bought furniture:")
if total_spent > 0:
    print("\n".join(furniture))
print(f"Total money spend: {total_spent:.2f}")
