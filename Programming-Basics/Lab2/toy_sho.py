needed_sum = float(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_toy_trucks = int(input())

puzzle_price = 2.60 * number_puzzle
dolls_price = 3 * number_dolls
bears_price = 4.10 * number_bears
minions_price = 8.20 * number_minions
toy_trucks_price = 2 * number_toy_trucks
total_income = puzzle_price + dolls_price + bears_price + minions_price + toy_trucks_price

total_toys = number_puzzle + number_dolls + number_bears + number_minions + number_toy_trucks
if total_toys >= 50:
    total_income_discount1 = total_income - 0.25 * total_income
total_income_discount2 = (total_income - 0.25 * total_income) - 0.10 * (total_income - 0.25 * total_income)
difference = abs(total_income_discount2 - needed_sum)
if total_income_discount2 >= needed_sum:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")