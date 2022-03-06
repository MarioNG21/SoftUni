command = input()

grocery_dict = {}

while command != "buy":
    product_name, price, qny = command.split()
    if product_name not in grocery_dict:
        grocery_dict[product_name] = []
        grocery_dict[product_name].append(int(qny))
        grocery_dict[product_name].append(float(price))
    elif product_name in grocery_dict:
        grocery_dict[product_name][0] += int(qny)
        grocery_dict[product_name].pop(1)
        grocery_dict[product_name].append(float(price))

    command = input()
for name, price_grocery in grocery_dict.items():
        quantity = price_grocery[0]
        price = price_grocery[1]
        sum_of_all = price * quantity
        print(f"{name} -> {sum_of_all:.2f}")