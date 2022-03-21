import math
figure = input("What is the figure? ")

if figure.lower() == "square":
    a = float(input("Side length: "))
    print(f"Area = {(a * a):.3f}")
elif figure.lower() == "rectangle":
    b = float(input("First side length: "))
    c = float(input("Second side length: "))
    print(f"Area = {b * c:.3f}")
elif figure.lower() == "circle":
    r = float(input("Radius length: "))
    print(f"Area = {math.pi * r ** 2:.3f}")
elif figure.lower() == "triangle":
    d = float(input("Side length: "))
    h = float(input("Height: "))
    print(f"Area = {(d * h) / 2:.3f}")
else:
    print("Figure can be: square, rectangle, circle or triangle.")
