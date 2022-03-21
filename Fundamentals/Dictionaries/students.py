text = input()
courses = {}

while ":" in text:

    data = text.split(":")  # (name, id, course) = text.split(":") SAME! and BETTER
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = {}

    courses[course][id] = name

    text = input()

course = " ".join(text.split("_"))  # text = text.replace("_", " "), does the same
# for key, value in courses.items():
#    if key == course:
#        for id, name in value.items():
#            print(f"{name} - {id}")
for id in courses[course]:
    print(f"{courses[course][id]} - {id}")
