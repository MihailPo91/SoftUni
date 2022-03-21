n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(n):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number < 400:
        p2 += 1
    elif 400 <= current_number < 600:
        p3 += 1
    elif 600 <= current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

percent1 = (p1 / n) * 100
percent2 = (p2 / n) * 100
percent3 = (p3 / n) * 100
percent4 = (p4 / n) * 100
percent5 = (p5 / n) * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")
