import math

tournaments = int(input())
starting_points = int(input())
played = 0
W = 0
F = 0
SF = 0

for num in range(tournaments):
    stage = input()
    if stage == "W":
        starting_points += 2000
        W += 1
    elif stage == "F":
        starting_points += 1200
        F += 1
    elif stage == "SF":
        starting_points += 720
        SF += 1

total_points = math.floor(starting_points)
average = math.floor((W * 2000 + F * 1200 + SF * 720) / tournaments)
win_percent = W / tournaments * 100

print(f"Final points: {starting_points}")
print(f"Average points: {average}")
print(f"{win_percent:.2f}%")



