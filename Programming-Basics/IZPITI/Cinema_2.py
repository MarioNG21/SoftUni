capacity = int(input())
command = input()
taken_places = 0
total_income = 0
while command != "Movie time!":
    number_of_customers = int(command)
    taken_places += number_of_customers
    if taken_places > capacity:
        print("The cinema is full.")
        break
    earned_money = number_of_customers * 5
    if number_of_customers % 3 == 0:
        earned_money -= 5
    total_income += earned_money
    command = input()
else:
    print(f"There are {capacity - taken_places} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")