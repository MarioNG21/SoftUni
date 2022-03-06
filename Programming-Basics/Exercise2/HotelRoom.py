# 2 вида стаи - студио и апартамент
# За студио, при повече от 7 нощувки през май и октомври : 5% намаление
# За студио, при повече от 14 нощувки през май и октомври : 30% намаление
# За студио, при повече от 14 нощувки през юни и септември: 20% намаление
# За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление
#
season = input()
number_of_accommodation = int(input())
if season == "May" or season == "October":
    studio = 50
    apartment = 65
    prize_for_studio = 50 * number_of_accommodation
    prize_for_apartment = 65 * number_of_accommodation
    if 7 < number_of_accommodation <= 14:
        prize_for_studio = prize_for_studio - prize_for_studio * 0.05
    if number_of_accommodation > 14:
        prize_for_studio = prize_for_studio - prize_for_studio * 0.3
        prize_for_apartment *= 0.9
    print(f"Apartment: {prize_for_apartment:.2f} lv.")
    print(f"Studio: {prize_for_studio:.2f} lv.")
if season == "June" or season == "September":
    studio = 75.20
    apartment = 68.70
    prize_for_studio = studio * number_of_accommodation
    prize_for_apartment = apartment * number_of_accommodation
    if number_of_accommodation > 14:
        prize_for_studio = prize_for_studio - prize_for_studio * 0.2
        prize_for_apartment *= 0.9
    print(f"Apartment: {prize_for_apartment:.2f} lv.")
    print(f"Studio: {prize_for_studio:.2f} lv.")
if season == "July" or season == "August":
    studio = 76
    apartment = 77
    prize_for_studio = studio * number_of_accommodation
    prize_for_apartment = apartment * number_of_accommodation
    if number_of_accommodation > 14:
        prize_for_apartment = prize_for_apartment - 0.1 * prize_for_apartment
    print(f"Apartment: {prize_for_apartment:.2f} lv.")
    print(f"Studio: {prize_for_studio:.2f} lv.")