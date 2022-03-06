# знаем наема
# статуиките са 30 % по малко от наема
#  кетъринг е 15 % по - малък от този на статуетката
#  озвучаването е 1/2 от цената на кетърнига

rent_money = int(input())
awards = rent_money - 0.3 * rent_money
food = awards - 0.15 * awards
music = 0.5 * food
print(f"{rent_money + awards + food + music:.2f}")
