# кучето и котката ядът различно количество храна от общата храна
# на всеки 3 дена получават награда бисквитка -> бисквитката е 10 % от изядената храна за деня
# колко бисквитки са изяли ,колко от зададената храна са изяли
# колко е изяло кучето в проценти
# колко е изяла котката в проценти
days = int(input())
whole_food = float(input())
dog_food_sum = 0
cat_food_sum = 0
biscuit_sum = 0
for day in range(1, days+1):
    dog_food = int(input())
    cat_food = int(input())
    eaten_food_for_the_day = cat_food + dog_food
    if day % 3 == 0:
        biscuit = round(0.1 * eaten_food_for_the_day)
        biscuit_sum += biscuit
    dog_food_sum += dog_food
    cat_food_sum += cat_food

eaten_food = dog_food_sum + cat_food_sum
eaten_food_in_percent = (eaten_food/whole_food) * 100
dog_food_in_percent = (dog_food_sum/eaten_food) * 100
cat_food_in_percent = (cat_food_sum/eaten_food) * 100
print(f"Total eaten biscuits: {biscuit_sum}gr.")
print(f"{eaten_food_in_percent:.2f}% of the food has been eaten.")
print(f"{dog_food_in_percent:.2f}% eaten from the dog.")
print(f"{cat_food_in_percent:.2f}% eaten from the cat.")
