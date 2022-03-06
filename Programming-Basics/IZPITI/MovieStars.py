
budget = float(input())
command = input()
while command != "ACTION":
    name = command
    length_name = len(name)
    if length_name > 15:
        wage = 0.2 * budget
    else:
        wage = float(input())
    budget -= wage
    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    command = input()
else:
    print(f"We are left with {budget:.2f} leva.")