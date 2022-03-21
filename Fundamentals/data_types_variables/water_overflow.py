flow_amount = int(input())

capacity = 255
current_amount = 0

for i in range(flow_amount):
    flow = int(input())
    current_amount += flow
    if current_amount > capacity:
        print("Insufficient capacity!")
        current_amount -= flow


print(current_amount)
