import re

main_pattern = r"[@][#]+[A-Z][A-Za-z0-9]{4,}[A-Z][@][#]+"

number = int(input())

for barcode in range(number):
    line = input()
    matched = re.findall(main_pattern, line)
    matched_nums = re.findall(r"\d", line)
    if len(matched_nums) > 0:
        product_group = ''.join(matched_nums)
    else:
        product_group = '00'

    if line == ''.join(matched):
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
        