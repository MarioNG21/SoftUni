# 1 minuta razhodka = 5 calorii
# razhodkata e ok ako 50 % procenta izgarq po vreme na razhodka

min_walk = int(input())
number_of_times_walk = int(input())
calorie_intake = int(input())

burned_calories = min_walk * 5
burned_calories_for_the_day = burned_calories * number_of_times_walk

if burned_calories_for_the_day >= (0.5 * calorie_intake):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories_for_the_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories_for_the_day}.")