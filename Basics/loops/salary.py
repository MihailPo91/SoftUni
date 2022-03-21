tabs = int(input())
salary = float(input())
fine = 0

for n in range(tabs):
    site = input()
    if site == "Facebook":
        fine += 150
    elif site == "Instagram":
        fine += 100
    elif site == "Reddit":
        fine += 50
    else:
        pass

diff = abs(fine - salary)

if fine >= salary:
    print("You have lost your salary.")
else:
    print(f"{diff:.0f}")