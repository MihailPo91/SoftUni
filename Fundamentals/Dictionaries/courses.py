courses_database = {}
students = []

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    else:
        course = command[0]
        name = command[1]

        if course not in courses_database:
            courses_database[course] = []
            courses_database[course].append(name)
        else:
            courses_database[course].append(name)
for key, value in courses_database.items():
    print(f"{key}: {len(value)}")
    for n in value:
        print(f"-- {n}")

