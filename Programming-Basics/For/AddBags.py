# до 10кг – 20% от цената на багаж над 20кг
# между 10кг и 20кг вкл. – 50% от цената на багаж над 20кг
# над 20кг – таксата се чете от конзолата
#


price_over_20_kg = float(input())
kg_of_bags = float(input())
days = int(input())
bags = int(input())
price = 0
# taxes
if kg_of_bags < 10:
    price = 0.2 * price_over_20_kg
elif 10 <= kg_of_bags <= 20:
    price = 0.5 * price_over_20_kg
elif kg_of_bags > 20:
    price = price_over_20_kg

if days > 30:
    price = price + 0.1 * price
elif 7 <= days <= 30:
    price = price + 0.15 * price
elif days < 7:
    price = price + 0.4 * price
price = price * bags
print(f"The total price of bags is: {price:.2f} lv. ")