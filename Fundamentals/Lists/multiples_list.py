factor = int(input())
count = int(input())

a_list = list()

for num in range(1, count + 1):
    a_list.append((num * factor))

print(a_list)
