budget = float(input())
season = input()
type_car = ""
name = ""
price = 0
if budget <= 100:
    type_car = "Economy class"
    if season == "Summer":
        name = "Cabrio"
        price = 0.35 * budget
    elif season == "Winter":
        name = "Jeep"
        price = 0.65 * budget
elif 100 < budget <= 500:
    type_car = "Compact class"
    if season == "Summer":
        name = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        name = "Jeep"
        price = 0.80 * budget
elif budget > 500:
    type_car = "Luxury class"
    if season == "Summer":
        name = "Jeep"
        price = 0.90 * budget
    elif season == "Winter":
        name = "Jeep"
        price = 0.90 * budget
print(f"{type_car}")
print(f"{name} - {price:.2f}")