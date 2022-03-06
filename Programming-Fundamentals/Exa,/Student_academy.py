counter = int(input())
academy_list = {}
new_list = {}
for i in range(counter):
    student = input()
    grade = float(input())
    if student not in academy_list:
        academy_list[student] = []
    academy_list[student].append(grade)

for key, value in academy_list.items():
    sum_of_student = 0
    for num in value:
        sum_of_student += num
    average_grade = sum_of_student / len(value)
    if average_grade >= 4.50:
        new_list[key] = average_grade

sorted_academy_list = sorted(new_list.items(), key=lambda kvp: -kvp[1])

for students, grades in sorted_academy_list:
    print(f"{students} -> {grades:.2f}")