names_count = int(input())
uniques = set()

for n in range(names_count):
    name = input()
    uniques.add(name)

for n in uniques:
    print(n)
