number_students = int(input())
students_data = {}

for student in range(number_students):
    name = input()
    grade = float(input())

    if name not in students_data:
        students_data[name] = []
        students_data[name].append(grade)

    else:
        students_data[name].append(grade)


for key in students_data:
    if sum(students_data[key]) / len(students_data[key]) >= 4.5:
        print(f"{key} -> {sum(students_data[key]) / len(students_data[key]):.2f}")
