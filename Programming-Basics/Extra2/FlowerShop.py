number_of_chrysanthemum = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday = input()

if season == "Summer" or season == "Spring":
    chrysanthemum = 2.00
    roses = 4.10
    tulips = 2.50
    if holiday == "Y":
        chrysanthemum = chrysanthemum + 0.15 * chrysanthemum
        roses = roses + 0.15 * roses
        tulips = tulips + 0.15 * tulips
    else:
        chrysanthemum = 2.00
        roses = 4.10
        tulips = 2.50
    price_for_chrysanthemum = chrysanthemum * number_of_chrysanthemum
    price_for_roses = roses * number_of_roses
    price_for_tulips = tulips * number_of_tulips
    sum = price_for_chrysanthemum + price_for_roses + price_for_tulips
    if number_of_tulips > 7 and season == "Spring":
        sum *= 0.95
    elif number_of_roses >= 10 and season == "Winter":
        sum *= 0.90
    if number_of_chrysanthemum + number_of_roses + number_of_tulips > 20:
        sum *= 0.80
    print(f"{sum + 2:.2f}")


if season == "Winter" or season == "Autumn":
    chrysanthemum = 3.75
    roses = 4.50
    tulips = 4.15
    if holiday == "Y":
        chrysanthemum = chrysanthemum + 0.15 * chrysanthemum
        roses = roses + 0.15 * roses
        tulips = tulips + 0.15 * tulips
    else:
        chrysanthemum = 3.75
        roses = 4.50
        tulips = 4.15
    price_for_chrysanthemum = chrysanthemum * number_of_chrysanthemum
    price_for_roses = roses * number_of_roses
    price_for_tulips = tulips * number_of_tulips
    sum = price_for_chrysanthemum + price_for_roses + price_for_tulips
    if number_of_tulips > 7 and season == "Spring":
        sum *= 0.95
    elif number_of_roses >= 10 and season == "Winter":
        sum *= 0.90
    if number_of_chrysanthemum + number_of_roses + number_of_tulips > 20:
        sum *= 0.80
    print(f"{sum + 2:.2f}")