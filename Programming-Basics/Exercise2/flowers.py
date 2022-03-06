# роза - 5 лв , далия - 3.8 , лале - 2,8
# крайна цена = брой на цветя по еденичната цена
# отстъпка -
# проверка за бюдет
type_flower = input()
count_flowers = int(input())
budget = int(input())
final_price = 0
if type_flower == "Roses":
    final_price = count_flowers * 5
    if count_flowers > 80:
        final_price = final_price - 0.1 * final_price
elif type_flower == "Dahlias":
    final_price = count_flowers * 3.8
    if count_flowers > 90:
        final_price *= 0.85
elif type_flower == "Tulips":
    final_price = count_flowers * 2.8
    if count_flowers > 80:
        final_price *= 0.85
elif type_flower == "Narcissus":
    final_price = count_flowers * 3
    if count_flowers < 120:
        final_price = final_price + 0.15 * final_price
elif type_flower == "Gladiolus":
    final_price = count_flowers * 2.5
    if count_flowers < 80:
        final_price = final_price + 0.2 * final_price
if budget >= final_price:
    left_money = budget - final_price
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {left_money:.2f} leva left.")
else:
    left_money= final_price - budget
    print(f"Not enough money, you need {left_money:.2f} leva more.")