n = int(input())
odd_sum = 0
even_sum = 0

for number in range(1, n + 1):
    element = int(input())
    if number % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

diff = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")



