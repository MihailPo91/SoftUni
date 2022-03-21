tax_year = int(input())
shoes = tax_year - tax_year * 0.40
jersey = shoes - shoes * 0.20
ball = jersey * 0.25
other = ball * 0.2

price = tax_year + shoes + jersey + ball + other
print(price)