data = input()
courses = {}

while ":" in data:
    student_name, i_d, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][i_d] = student_name

    data = input()


searched_course = data
searched_course_name_as_list = searched_course.split("_")
searched_course = ' '.join(searched_course_name_as_list)

for course_info in courses:
    if course_info == searched_course:
        for i_d, name in courses[course_info].items():
            print(f"{name} - {i_d}")