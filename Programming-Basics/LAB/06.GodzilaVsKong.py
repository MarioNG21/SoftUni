budget = float(input())
count_statist = int(input())
price_per_statist = float(input())

price_decor = 0.1 * budget
price_clothes = count_statist * price_per_statist
if count_statist > 150:
    price_clothes *= 0.9
    #price_clothes *= 0.85
expenses = price_decor + price_clothes
if expenses > budget:
    print("Not enough money!")
    needed_money = expenses - budget
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    print("Action!")
    left_money = budget - expenses
    print(f"Wingard starts filming with {left_money:.2f} leva left.")