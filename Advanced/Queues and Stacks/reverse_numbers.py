input_data = input().split()
reversed_data = []

for n in range(len(input_data)):
    reversed_data.append(int(input_data[n]))

for n in range(len(reversed_data)):
    print(reversed_data.pop(), end=' ')
