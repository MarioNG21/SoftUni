minutes_per_walk = int(input())
number_of_walks = int(input())
calories_intake_per_day = int(input())
burned_calories = number_of_walks * minutes_per_walk * 5
if burned_calories >= (calories_intake_per_day * 0.5):
    print()
else:
