import sys

n = int(input())
total_sum = 0
max_number = -sys.maxsize

for num in range(1, n + 1):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    total_sum += current_number

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")

else:
    print("No")
    print(f"Diff = {abs(max_number - (total_sum - max_number))}")