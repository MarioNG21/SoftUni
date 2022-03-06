# 3 типа билети  студентски , детски и стандартен
# външен цикъл  до получаване на командта финиш се чете филм
# continue : command != Finish
# stop : command == Finish
# тази команда е и име на филм
first_command = input()
overall_tickets = 0
students = 0
kids = 0
standard = 0
while first_command != "Finish":
    movie = first_command
    free_places = int(input())
    second_command = input()
    taken_places = 0
    while second_command != "End":
        ticket_type = second_command
        if ticket_type == "student":
            students += 1
            taken_places += 1
        elif ticket_type == "standard":
            standard += 1
            taken_places += 1
        elif ticket_type == "kid":
            kids += 1
            taken_places += 1
        if taken_places >= free_places:
            break
        second_command = input()
    print(f"{movie} - {(taken_places/free_places)* 100:.2f}% full.")
    first_command = input()
else:
    overall = kids + standard + students
    print(f"Total tickets: {overall}")
    print(f"{(students/overall)* 100:.2f}% student tickets.")
    print(f"{(standard/overall)* 100:.2f}% standard tickets.")
    print(f"{(kids/overall)* 100:.2f}% kids tickets.")