def tribonacci(number):
    new_list = [0] * number
    new_list[0] = 1
    new_list[1] = 1
    new_list[2] = 2
    for i in range(3, number):
        new_list[i] = new_list[i - 3] + new_list[i - 2] + new_list[i - 1]
    print(*new_list, sep=" ")


num = int(input())

if num < 3:
    for i in range(-1, num-1):
        print(1,end=" ")
    print()
else:
    tribonacci(num)
