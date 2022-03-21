city = input()
sales = float(input())
trade_commissions = 0
value = True

if city == "Sofia":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.05
    elif 500 < sales <= 1000:
        trade_commissions = sales * 0.07
    elif 1000 < sales <= 10000:
        trade_commissions = sales * 0.08
    elif sales > 10000:
        trade_commissions = sales * 0.12
    else:
        value = False
elif city == "Varna":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.045
    elif 500 < sales <= 1000:
        trade_commissions = sales * 0.075
    elif 1000 < sales <= 10000:
        trade_commissions = sales * 0.10
    elif sales > 10000:
        trade_commissions = sales * 0.13
    else:
        value = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        trade_commissions = sales * 0.055
    elif 500 < sales <= 1000:
        trade_commissions = sales * 0.08
    elif 1000 < sales <= 10000:
        trade_commissions = sales * 0.12
    elif sales > 10000:
        trade_commissions = sales * 0.145
    else:
        value = False
else:
    value = False

if value:
    print(f"{trade_commissions:.2f}")
else:
    print("error")
