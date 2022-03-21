lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

V_litres = (lenght * width * height) / 1000
taken_space = V_litres * (percent / 100)
total_needed = V_litres - taken_space
print(total_needed)
