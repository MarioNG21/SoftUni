budget = float(input())
number_of_series = int(input())
sum_price = 0
for series in range(1,number_of_series+1):
    name = input()
    price = float(input())
    if name == "Thrones":
        price = price - 0.5 * price
    elif name == "Lucifer":
        price = price - 0.4 * price
    elif name == "Protector":
        price = price - 0.3 * price
    elif name == "TotalDrama":
        price = price - 0.2 * price
    elif name == "Area":
        price = price - 0.1 * price
    sum_price += price
if budget >= sum_price:
    diff = budget - sum_price
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    needed_money = sum_price - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")