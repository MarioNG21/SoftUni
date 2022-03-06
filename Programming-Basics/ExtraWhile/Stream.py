#редуват се плащане в брой с плащане с карта
# ако цената е над 100 лв не може в брой
# ако цената е под 10 лв не може с карта
# stop : command == End или до достигане на сумата
# continue : command != End или при недостигната сума
upcoming_money = int(input())
pay_with_card = 0
sum_with_card = 0
pay_with_cash = 0
sum_cash = 0
collected_money = 0
command = ""
counter = 0

while collected_money < upcoming_money:
    command = input()
    if command == "End":
        if collected_money < upcoming_money:
            print("Failed to collect required money for charity.")
            break
    price = int(command)
    counter += 1
    if counter % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            pay_with_cash += 1
            sum_cash += price
    elif counter % 2 == 0:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            pay_with_card += 1
            sum_with_card += price
    collected_money = sum_cash + sum_with_card
    if collected_money >= upcoming_money:
        print(f"Average CS: {(sum_cash/pay_with_cash):.2f}")
        print(f"Average CC: {(sum_with_card/ pay_with_card):.2f}")
        break
