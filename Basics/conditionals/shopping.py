budget = float(input())
number_videocards = int(input())
number_processors = int(input())
number_ram = int(input())
price_video = number_videocards * 250
price_processor = (price_video * 0.35) * number_processors
price_ram = (price_video * 0.10) * number_ram
total_price = price_video + price_processor + price_ram


if number_videocards > number_processors:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)

if budget < total_price:
    print(f"Not enough money! You need {diff:.2f} leva more!")
elif budget >= total_price:
    print(f"You have {diff:.2f} leva left!")