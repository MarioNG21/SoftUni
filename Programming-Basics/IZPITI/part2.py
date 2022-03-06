budget = float(input())
total = 0
command = input()
counter = 0
while command != 'Stop':
    name_of_product = command
    price = float(input())
    total += price
    counter += 1
    if counter % 3 == 0:
        total -= price / 2
    if budget < total:
        print("You don't have enough money!")
        print(f"You need {total - budget:.2f} leva!")
        break
    command = input()
if command == 'Stop':
    print(f"You bought {counter} products for {total:.2f} leva.")
