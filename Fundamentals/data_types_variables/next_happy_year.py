year = int(input())

is_year_happy = False

while not is_year_happy:
    year += 1
    str_year = str(year)
    set_year = set()
    for i in range(len(str_year)):
        set_year.add(str_year[i])
    # Може да се направи и директно със set(str(year)) и директно ще пълним сета с елементите
    if len(str_year) == len(set_year):
        is_year_happy = True
    # може и със: is_year_happy = len(str_year) == len(set_year): ако искаме да е по опростено
print(year)