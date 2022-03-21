import sys

from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("Enter the ammount:  "))
from_currency = input("From currency:  ").upper()
to_currency = input("To currency:  ").upper()

print(amount, from_currency, "<----- To ----->", to_currency)

result = c.convert(from_currency, to_currency, amount)

print(f"{result:.2f} {to_currency}")

ready = input("Are you ready? Y/N  ").upper()
if ready == "Y":
    sys.exit()

while ready == "N":

    c = CurrencyRates()
    amount = int(input("Enter the ammount:  "))
    from_currency = input("From currency:  ").upper()
    to_currency = input("To currency:  ").upper()

    print(amount, from_currency, "<----- To ----->", to_currency)

    result = c.convert(from_currency, to_currency, amount)

    print(f"{result:.3f} {to_currency}")

    ready = input("Are you ready? Y/N  ").upper()

