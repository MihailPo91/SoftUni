age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        print("Mr.")
    if age < 16:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    if age < 16:
        print("Miss")