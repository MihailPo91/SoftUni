n = int(input())
total_sum_left = 0
total_sum_right = 0

for number in range(1, n + 1):
    value_left = int(input())
    total_sum_left += value_left

for number in range(1, n + 1):
    value_right = int(input())
    total_sum_right += value_right

diff = abs(total_sum_right - total_sum_left)

if total_sum_left == total_sum_right:
    print(f"Yes, sum = {total_sum_right}")
elif total_sum_right != total_sum_left:
    print(f"No, diff = {diff}")

