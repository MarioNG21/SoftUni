counter = int(input())
grades_dict = {}


def avg(values):
    return  sum(values) / len(values)


for _ in range(counter):
    student_name, grade = input().split()
    student_grade = float(grade)
    if student_name not in grades_dict:
        grades_dict[student_name] = []
    grades_dict[student_name].append(student_grade)

for n, g in grades_dict.items():
    avg_grade = avg(g)

    grade_str = ' '.join(str(f'{x:.2f}') for x in g)

    print(f"{n} -> {grade_str} (avg: {avg_grade:.2f})")