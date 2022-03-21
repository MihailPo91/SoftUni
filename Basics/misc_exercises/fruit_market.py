strawberry_price = float(input())
bananas_quant = float(input())
orange_quant = float(input())
raspberry_quant = float(input())
strawberry_quant = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (raspberry_price * 0.40)
banana_price = raspberry_price - (raspberry_price * 0.80)

total_price = strawberry_quant * strawberry_price + raspberry_price * raspberry_quant \
    + orange_price * orange_quant + banana_price * bananas_quant

print(f"{total_price:.2f}")

