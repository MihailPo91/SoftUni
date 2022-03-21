month = input()
overnights = int(input())
studio_price = 0
apartment_price = 0


if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < overnights < 14:
        studio_price -= studio_price * 0.05
    if overnights > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10
if month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if overnights > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10
if month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if overnights > 14:
        apartment_price -= apartment_price * 0.10

costs_studio = overnights * studio_price
costs_apartment = overnights * apartment_price

print(f"Apartment: {costs_apartment:.2f} lv.")
print(f"Studio: {costs_studio:.2f} lv.")



