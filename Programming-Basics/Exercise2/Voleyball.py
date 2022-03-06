# волейбол през уикендите и през празничните дни
# всяка събота като не пътува обратно за родния си град и не е на работа играе волейбол
# 2/3 от празничните дни играе
# h пъти пътува до родния си град където играе в неделя волейбол
# 3/4 от уикендите не е на работа в които е в софия
# през високосните години играе 15 процента повече
# 48 подходящи уикенда за волейбол
# да закръгля до долното чисf
import math
type_year = input()
number_rest_days = int(input())
number_of_weekends = int(input())

number_of_weekends_in_Sofia = 48 - number_of_weekends
number_of_weekends_for_play = 3/4 * number_of_weekends_in_Sofia
number_of_rest_day_for_play = 2/3 * number_rest_days

if type_year == "leap":
    sum = number_of_weekends_for_play + number_of_rest_day_for_play + number_of_weekends
    sum_plus_percent = sum + 0.15 * sum
    print(f"{math.floor(sum_plus_percent)}")
elif type_year == "normal":
    sum = number_of_weekends_for_play + number_of_rest_day_for_play + number_of_weekends
    print(f"{math.floor(sum)}")

