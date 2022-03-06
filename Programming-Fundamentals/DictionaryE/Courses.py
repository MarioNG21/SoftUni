cmd = input()

courses = {}

while cmd != "end":
    command = cmd.split(" : ")
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses:
        courses[course_name] = []
    if student_name not in courses[course_name]:
        courses[course_name].append(student_name)

    cmd = input()

courses_dict = sorted(courses.items(), key=lambda kvp: (-len(kvp[1])))
for key, value in courses_dict:
        print(f"{key}: {len(value)}")
        sorted_values = sorted(value, key=lambda x: x[0])
        for _ in range(0, len(sorted_values)):
            first_name = sorted_values[_]
            print(f"-- {''.join(first_name)}")