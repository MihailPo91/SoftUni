n = int(input())

positives_list = []
negatives_list = []
negatives_sum = 0

for element in range(1, n+1):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)
        negatives_sum += number

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {negatives_sum}")
