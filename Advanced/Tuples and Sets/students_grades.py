def avg(values):
    return sum(values) / len(values)


students_number = int(input())
student_dict = {}

for line in range(students_number):
    student, grade = input().split(' ')
    if student not in student_dict:
        student_dict[student] = []
    student_dict[student].append(float(grade))


for student, grades in student_dict.items():
    grade_average = avg(grades)
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{student} -> {grades_formatted} (avg: {grade_average:.2f})')
