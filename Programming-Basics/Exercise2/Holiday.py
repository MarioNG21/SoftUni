# при 100 лв или по малко някъде в България - лято 30 пр. от бюджета зима 70 процента
# при 1000 лв или по малко - лято 40 пр а зима 80 процента
# при повече от 1000 лв - 90 процента от бюджета
#
budget = float(input())
season = input()

if budget <= 100:
    if season == "summer":
        type_holiday = "Camp"
        given_money = budget * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"{type_holiday} - {given_money:.2f}")
    if season == "winter":
        type_holiday = "Hotel"
        given_money =  budget * 0.7
        print(f"Somewhere in Bulgaria")
        print(f"{type_holiday} - {given_money:.2f}")
if budget <= 1000 and budget > 100:
    if season == "summer":
        type_holiday = "Camp"
        given_money = budget * 0.4
        print(f"Somewhere in Balkans")
        print(f"{type_holiday} - {given_money:.2f}")
    if season == "winter":
        type_holiday = "Hotel"
        given_money = budget * 0.8
        print(f"Somewhere in Balkans")
        print(f"{type_holiday} - {given_money:.2f}")
if budget > 1000:
    if season == "summer" or season == "winter":
        type_holiday = "Hotel"
        given_money = 0.9 * budget
        print(f"Somewhere in Europe")
        print(f"{type_holiday} - {given_money:.2f}")