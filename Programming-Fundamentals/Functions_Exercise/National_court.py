first_employee_counter = int(input())
second_employee_counter = int(input())
third_employee_counter = int(input())
people_count = int(input())

max_answers_per_hour = first_employee_counter + second_employee_counter + third_employee_counter

hours = 1
counter = 0

def answered_calls(hour: int, max_answers: int, max_people: int, count: int):
    while max_people > 0:
        count += 1
        if count % 4 == 0:
            continue
        max_people -= (hour * max_answers)

    return count


time = (answered_calls(hours, max_answers_per_hour, people_count, counter))

print(f"Time needed: {time}h.")