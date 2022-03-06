# cenata e ravna na duljinata na imeto mu
# ako centa e nechetna ima 25 procenta otstupka
# stop: command = "Party!"
# stop: earned_money >= needed_money
# continue : pri obratnite usloviq
goal_money = float(input())
command = input()
goal_reached = False
whole_income = 0
while command != "Party!":
    name = command
    amount_drinks = int(input())
    price_drink = len(name)
    price = price_drink * amount_drinks
    income = 0
    if price % 2 == 1:
        price = price - 0.25 * price
        income += price
        goal_money -= income
    else:
        income += price
        goal_money -= income
    whole_income += income
    if goal_money <= 0:
        goal_reached = True
        break
    command = input()
if goal_reached:
    print("Target acquired.")
else:
    print(f"We need {goal_money:.2f} leva more.")
print(f"Club income - {whole_income:.2f} leva.")