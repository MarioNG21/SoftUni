# наем -> зависи от сезона
# отстъпка -> броя на хората
# допълнителна отстъпка ->
# бюджета дали стига
# пролет -> 3000 лв
#  лято и есен - 4200
# зима ->  2600
#
budget = int(input())
season = input()
number_fisherman = int(input())
rent = 0
if season == "Spring":
    rent = 3000
if season == "Summer" or season == "Autumn":
    rent = 4200
if season == "Winter":
    rent = 2600
if number_fisherman <= 6:
    rent *= 0.9
elif 7 <= number_fisherman <= 11:
    rent *= 0.85
elif number_fisherman >= 12:
    rent *= 0.75
if number_fisherman % 2 == 0 and season != "Autumn":
    rent *= 0.95
if budget >= rent:
    left_money = budget - rent
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = rent - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")