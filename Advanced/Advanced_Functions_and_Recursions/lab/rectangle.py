def rectangle(length, width):
    def area(length, width):
        return length * width

    def perimeter(length, width):
        return 2 * (length + width)

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    else:
        return f'''Rectangle area: {area(length, width)}
Rectangle perimeter: {perimeter(length, width)}'''


print(rectangle(2, 10))

print(rectangle('2', 10))
