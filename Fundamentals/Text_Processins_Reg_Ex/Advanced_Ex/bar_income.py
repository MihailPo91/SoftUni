import re

pattern_name = r"[%]([A-Z][a-z]+)[%]"
pattern_product = r"[<](\w+)[>]"
pattern_amount = r"[|](\d+)[|]"
pattern_price = r"(.*)[|>%](\d{1,}[.]?\d+?)[$]"

pattern = r"[%]([A-Z][a-z]+)[%](.*)[<](\w+)[>](.*)[|](\d+)[|](.*)(\d+[.]?\d+)[$]"

total_income = 0
price = 0.0

command = input()

while command != "end of shift":
    is_valid = False
    check_validation = [el for el in re.findall(pattern, command)]
    if len(check_validation) > 0 and "" not in check_validation:
        is_valid = True
    if is_valid:
        name = ''.join(re.findall(pattern_name, command))
        product = ''.join(re.findall(pattern_product, command))
        amount = int(''.join(re.findall(pattern_amount, command)))
        for el in check_validation:
            for e in el:
                if "." in e:
                    price = float(''.join([gr.group(2) for gr in re.finditer(pattern_price, command)]))
                else:
                    price = float(check_validation[0][-1])
        print(f"{name}: {product} - {(amount * price):.2f}")
        total_income += (amount * price)

    command = input()

print(f"Total income: {total_income:.2f}")
