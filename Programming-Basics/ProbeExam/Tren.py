from math import ceil
number_of_days = int(input())
run_km_first_day = float(input())
one_more_day = run_km_first_day
whole_sum_for_next_days = 0
for day in range(1, number_of_days+1):
    increase_percent = int(input())
    run_km_first_day += (increase_percent / 100) * run_km_first_day
    whole_sum_for_next_days += run_km_first_day
whole_sum_for_next_days += one_more_day
if whole_sum_for_next_days >= 1000:
    diff = whole_sum_for_next_days - 1000
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    diff = 1000 - whole_sum_for_next_days
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")