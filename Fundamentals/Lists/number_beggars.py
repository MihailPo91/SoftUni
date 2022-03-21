numbers = input().split(", ")
beggars = int(input())
result_sum = 0
result_list = []

for n in range(beggars):
    for i in range(n, len(numbers), beggars):
        result_sum += int(numbers[i])
    result_list.append(result_sum)
    result_sum = 0

print(result_list)




