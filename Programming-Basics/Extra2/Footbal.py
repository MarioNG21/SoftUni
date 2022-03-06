budget = float(input())
type_of_tickets = input()
number_of_people = int(input())
tickets = 0
if type_of_tickets == "VIP":
    tickets = 499.99
elif type_of_tickets == "Normal":
    tickets = 249.99
if 1 <= number_of_people <= 4:
    transport_price = budget * 0.75
    budget = budget - transport_price
    tickets = tickets * number_of_people
    if budget >= tickets:
        left_money = budget - tickets
        print(f"Yes! You have {left_money:.2f} leva left.")
    else:
        left_money = tickets - budget
        print(f"Not enough money! You need {left_money:.2f} leva.")
if 5 <= number_of_people <= 9:
    transport_price = budget * 0.6
    budget = budget - transport_price
    tickets = tickets * number_of_people
    if budget >= tickets:
        left_money = budget - tickets
        print(f"Yes! You have {left_money:.2f} leva left.")
    else:
        left_money = tickets - budget
        print(f"Not enough money! You need {left_money:.2f} leva.")
if 10 <= number_of_people <= 24:
    transport_price = budget * 0.5
    budget = budget - transport_price
    tickets = tickets * number_of_people
    if budget >= tickets:
        left_money = budget - tickets
        print(f"Yes! You have {left_money:.2f} leva left.")
    else:
        left_money = tickets - budget
        print(f"Not enough money! You need {left_money:.2f} leva.")
if 25 <= number_of_people <= 49:
    transport_price = 0.4 * budget
    budget = budget - transport_price
    tickets = tickets * number_of_people
    if budget >= tickets:
        left_money = budget - tickets
        print(f"Yes! You have {left_money:.2f} leva left.")
    else:
        left_money = tickets - budget
        print(f"Not enough money! You need {left_money:.2f} leva.")
if number_of_people >= 50:
    transport_price = 0.25 * budget
    budget = budget - transport_price
    tickets = tickets * number_of_people
    if budget >= tickets:
        left_money = budget - tickets
        print(f"Yes! You have {left_money:.2f} leva left.")
    else:
        left_money = tickets - budget
        print(f"Not enough money! You need {left_money:.2f} leva.")