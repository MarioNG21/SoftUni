# стойноста на екипировката да я намерим
# да намерим дали бюджета е достатъчен или не
# промоции:
#  ->всеки трети продукт е на половин цена

budget = float(input())
command = input()
has_money = True
left_price_product = 0
product_counter = 0
while command != "Stop":
    product = command
    price_product = float(input())
    product_counter += 1
    left_price_product += price_product
    if product_counter % 3 == 0:
        left_price_product -= price_product / 2
    if left_price_product > budget:
        left_money = left_price_product - budget
        has_money = False
        break
    command = input()
else:
    print(f"You bought {product_counter} products for {left_price_product:.2f} leva.")
if has_money == False:
    print("You don't have enough money!")
    print(f"You need {left_money:.2f} leva!")
