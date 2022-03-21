groups = int(input())
total_climbers = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0


for number in range(groups):
    climbers = int(input())
    total_climbers += climbers
    if climbers <= 5:
        g1 += climbers
    elif 5 < climbers <= 12:
        g2 += climbers
    elif 12 < climbers <= 25:
        g3 += climbers
    elif 25 < climbers <= 40:
        g4 += climbers
    else:
        g5 += climbers

g1 = g1 / total_climbers * 100
g2 = g2 / total_climbers * 100
g3 = g3 / total_climbers * 100
g4 = g4 / total_climbers * 100
g5 = g5 / total_climbers * 100

print(f"{g1:.2f}%")
print(f"{g2:.2f}%")
print(f"{g3:.2f}%")
print(f"{g4:.2f}%")
print(f"{g5:.2f}%")
