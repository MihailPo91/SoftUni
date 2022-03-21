string_numbers = list(map(int, input().split(", ")))
even_indices = list()

for i in range(len(string_numbers)):
    if string_numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
