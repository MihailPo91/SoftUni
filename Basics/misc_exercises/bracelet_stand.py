pocket_money = float(input())
sales_money = float(input())
costs = float(input())
gift_price = float(input())


income = (pocket_money * 5 + sales_money * 5) - costs
diff = abs(income - gift_price)

if income >= gift_price:
    print(f"Profit: {income:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")

