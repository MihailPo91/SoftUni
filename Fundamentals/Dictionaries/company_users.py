company_data = {}

while True:
    input_data = input().split(" -> ")
    if input_data[0] == "End":
        break
    company = input_data[0]
    id_number = input_data[1]

    if company not in company_data:
        company_data[company] = []
        if id_number not in company_data[company]:
            company_data[company].append(id_number)
    else:
        if id_number not in company_data[company]:
            company_data[company].append(id_number)

for key, value in company_data.items():
    print(f"{key}")
    for n in value:
        print(f"-- {n}")