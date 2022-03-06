
number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_road = input()

if type_of_road == "trail":
    charge_for_juniors = 5.50
    charge_for_seniors = 7
    sum_for_juniors = number_of_juniors * charge_for_juniors
    sum_for_seniors = number_of_seniors * charge_for_seniors
    whole_money = sum_for_seniors + sum_for_juniors
    expenses = whole_money * 0.05
    whole_money = whole_money - expenses
    print(f"{whole_money:.2f}")
if type_of_road == "cross-country":
    charge_for_juniors = 8
    charge_for_seniors = 9.50
    if number_of_seniors + number_of_juniors > 50:
        charge_for_juniors *= 0.75
        charge_for_seniors *= 0.75
    sum_for_juniors = number_of_juniors * charge_for_juniors
    sum_for_seniors = number_of_seniors * charge_for_seniors
    whole_money = sum_for_seniors + sum_for_juniors
    expenses = whole_money * 0.05
    whole_money = whole_money - expenses
    print(f"{whole_money:.2f}")
if type_of_road == "downhill":
    charge_for_juniors = 12.25
    charge_for_seniors = 13.75
    sum_for_juniors = number_of_juniors * charge_for_juniors
    sum_for_seniors = number_of_seniors * charge_for_seniors
    whole_money = sum_for_seniors + sum_for_juniors
    expenses = whole_money * 0.05
    whole_money = whole_money - expenses
    print(f"{whole_money:.2f}")
if type_of_road == "road":
    charge_for_juniors = 20
    charge_for_seniors = 21.50
    sum_for_juniors = number_of_juniors * charge_for_juniors
    sum_for_seniors = number_of_seniors * charge_for_seniors
    whole_money = sum_for_seniors + sum_for_juniors
    expenses = whole_money * 0.05
    whole_money = whole_money - expenses
    print(f"{whole_money:.2f}")