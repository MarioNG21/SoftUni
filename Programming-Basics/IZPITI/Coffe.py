drink = input()
sugar = input()
amount_drinks = int(input())
whole_price = 0
if sugar == "Without":
    if drink == "Espresso":
        price = 0.9
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if amount_drinks >= 5:
            whole_price = whole_price - 0.25 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Cappuccino":
        price = 1.00
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Tea":
        price = 0.5
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
elif sugar == "Normal":
    if drink == "Espresso":
        price = 1
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if amount_drinks >= 5:
            whole_price = whole_price - 0.25 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Cappuccino":
        price = 1.20
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Tea":
        price = 0.6
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
             whole_price = whole_price - 0.2 * whole_price
elif sugar == "Extra":
    if drink == "Espresso":
        price = 1.2
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if amount_drinks >= 5:
            whole_price = whole_price - 0.25 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Cappuccino":
        price = 1.60
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
    elif drink == "Tea":
        price = 0.7
        whole_price = price * amount_drinks
        if sugar == "Without":
            whole_price = whole_price - 0.35 * whole_price
        if whole_price > 15:
            whole_price = whole_price - 0.2 * whole_price
print(f"You bought {amount_drinks} cups of {drink} for {whole_price:.2f} lv.")