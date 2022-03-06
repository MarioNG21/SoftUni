unwanted_mark = int(input())
amount_unwanted_marks = 0
number = 0
sum_of_tasks = 0
sum_of_grades = 0
last_problem = ""
while amount_unwanted_marks < unwanted_mark:
    name_of_task = input()
    if name_of_task == "Enough":
        break
    number += 1
    mark = int(input())
    if mark <= 4:
        amount_unwanted_marks += 1
    sum_of_grades += mark
    sum_of_tasks += 1
    last_problem = name_of_task
else:
    print(f"You need a break, {amount_unwanted_marks} poor grades.")
if amount_unwanted_marks < unwanted_mark:
    print(f"Average score: {sum_of_grades/ number:.2f}")
    print(f"Number of problems: {sum_of_tasks}")
    print(f"Last problem: {last_problem}")

