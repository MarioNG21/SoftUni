# разфасовка 2 бр.
# разфасовка 5 бр.
# цената зависи от плодовете
#  спрямо разфасовката се определя цената
#  чете се броя разфасовки които тря да умножим по цената за да получим крайната цена
#  от 400 до 1000 включително се прави отсъпка
#  над 1000 се прави 50 процента отстъпка

type_fruit = input()
size = input()
orders = int(input())
whole_price = 0
if type_fruit == "Watermelon":
    if size == "small":
        price = 56 # на брой
        price = price * 2
        whole_price = price * orders
    elif size == "big":
        price = 28.70
        price = price * 5
        whole_price = price * orders

if type_fruit == "Mango":
    if size == "small":
        price = 36.66 # на брой
        price = price * 2
        whole_price = price * orders
    elif size == "big":
        price = 19.60
        price = price * 5
        whole_price = price * orders


if type_fruit == "Pineapple":
    if size == "small":
        price = 42.10 # на брой
        price = price * 2
        whole_price = price * orders
    elif size == "big":
        price = 24.80
        price = price * 5
        whole_price = price * orders



if type_fruit == "Raspberry":
    if size == "small":
        price = 20 # на брой
        price = price * 2
        whole_price = price * orders
    elif size == "big":
        price = 15.20
        price = price * 5
        whole_price = price * orders

if 400 <= whole_price <= 1000:
    whole_price = whole_price - 0.15 * whole_price
elif whole_price > 1000:
    whole_price = whole_price - 0.5 * whole_price
print(f"{whole_price:.2f} lv.")