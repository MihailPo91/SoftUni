results_data = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    if "banned" not in command:
        data = command.split("-")
        name = data[0]
        tech = data[1]
        result = int(data[2])

        if tech not in results_data:
            results_data[tech] = {name: result}
            submissions[tech] = 1
        else:
            if name not in results_data[tech]:
                results_data[tech][name] = result
                submissions[tech] += 1
            else:
                if result > results_data[tech][name]:
                    results_data[tech][name] = result
                    submissions[tech] += 1
                else:
                    submissions[tech] += 1

    elif "banned" in command:
        data = command.split("-")
        name = data[0]
        for key, values in results_data.items():
            if name in values:
                del results_data[key][name]

print("Results:")
for key, value in results_data.items():
    for v in value:
        print(f"{v} | {value[v]}")
print("Submissions:")
for key in submissions:
    print(f"{key} - {submissions[key]}")
