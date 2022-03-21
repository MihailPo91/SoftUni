N1 = int(input())
N2 = int(input())
operator = input()
type_number = ""

if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        type_number = "even"
    elif result % 2 == 1:
        type_number = "odd"
    print(f"{N1} {operator} {N2} = {result} - {type_number}")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        type_number = "even"
    elif result % 2 == 1:
        type_number = "odd"
    print(f"{N1} {operator} {N2} = {result} - {type_number}")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        type_number = "even"
    elif result % 2 == 1:
        type_number = "odd"
    print(f"{N1} {operator} {N2} = {result} - {type_number}")
if operator == "/":
    if N2 != 0:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")
elif operator == "%":
    if N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")






