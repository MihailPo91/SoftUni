resources = {}

while True:
    resource = input()
    if "stop" in resource:
        break
    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for key in resources:
    print(f"{key} -> {resources[key]}")
