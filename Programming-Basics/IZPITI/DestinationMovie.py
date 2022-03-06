budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
price = 0
whole_price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000
        whole_price = price * number_of_days
        whole_price = whole_price - 0.3 * whole_price
    elif season == "Summer":
        price = 40000
        whole_price = price * number_of_days
        whole_price = whole_price - 0.3 * whole_price
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
        whole_price = price * number_of_days
        whole_price = whole_price + 0.25 * whole_price
    elif season == "Summer":
        price = 12500
        whole_price = price * number_of_days
        whole_price = whole_price + 0.25 * whole_price
elif destination == "London":
    if season == "Winter":
        price = 24000
        whole_price = price * number_of_days

    elif season == "Summer":
        price = 20250
        whole_price = price * number_of_days
if budget >= whole_price:
    diff = budget - whole_price
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    diff = whole_price - budget
    print(f"The director needs {diff:.2f} leva more!")