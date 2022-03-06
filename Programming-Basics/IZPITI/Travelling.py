first_command = input()
while first_command != "End":
    place = first_command
    min_budget = float(input())
    saved_money = 0
    while saved_money < min_budget:
        savings = float(input())
        saved_money += savings
        if saved_money >= min_budget:
            break
    print(f"Going to {place}!")
    first_command = input()

