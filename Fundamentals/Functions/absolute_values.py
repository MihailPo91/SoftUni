nums = input().split(" ")
abs_list = []

for num in nums:
    abs_list.append(abs(float(num)))

print(abs_list)