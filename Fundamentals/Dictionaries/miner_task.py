resources = {}
metals = []
quantities = []

while True:
    command = input()
    if command == "stop":
        break
    else:
        if command.isdigit():
            quantities.append(int(command))
        else:
            metals.append(command)

for (i, f) in zip(metals, quantities):
    if i not in resources:
        resources[i] = f
    else:
        resources[i] += f

for key in resources:
    print(f"{key} -> {resources[key]}")
