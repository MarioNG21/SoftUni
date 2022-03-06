age = int(input())
laundry_price = float(input())
toy_prize = int(input())
birthday_money = 0
total_money = 0
total_toys = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        birthday_money = birthday_money + 10
        total_money = total_money + (birthday_money - 1)
    else:
        total_toys = total_toys + 1
sum_for_toys = total_toys * toy_prize
total_money = total_money + sum_for_toys
if total_money >= laundry_price:
    dif = total_money - laundry_price
    print(f"Yes! {dif:.2f}")
else:
    dif = laundry_price - total_money
    print(f"No! {dif:.2f}" )