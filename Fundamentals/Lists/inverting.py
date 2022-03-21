nums = input().split(' ')
new_list = list()

for n in nums:
    if int(n) > 0:
        new_list.append(-int(n))
    else:
        new_list.append(abs(int(n)))

print(new_list)