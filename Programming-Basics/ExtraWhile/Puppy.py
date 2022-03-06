food = int(input())
food_in_grams = food * 1000
command = input()
eaten_food_per_day = 0
while command != "Adopted":
    eaten_food = int(command)
    eaten_food_per_day += eaten_food
    command = input()
else:
    if eaten_food_per_day <= food_in_grams:
        left_overs = food_in_grams - eaten_food_per_day
        print(f"Food is enough! Leftovers: {left_overs} grams." )
    else:
        needed_food = eaten_food_per_day - food_in_grams
        print(f"Food is not enough. You need {needed_food} grams more." )