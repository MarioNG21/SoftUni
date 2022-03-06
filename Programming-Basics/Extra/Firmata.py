# 10 procenta ot dnite ne mogat da rabotqt po proekta
# raboten den 8 chasa
# 2 chasa izvun rabotno vreme za vseki slujitel
# chasovete sa zakrugleni kum po malkoto
import math
needed_hours = int(input())
days = int(input())
amount_of_workers = int(input())
days_for_work = days - 0.10 * days
days_in_hours = days_for_work * 8
overtime_work = amount_of_workers * 2 * days

sum_of_days = days_in_hours + overtime_work

if sum_of_days > needed_hours:
    hours = sum_of_days - needed_hours
    print(f"Yes!{math.floor(hours)} hours left.")

elif sum_of_days <= needed_hours:
    hours = needed_hours - sum_of_days
    print(f"Not enough time!{math.ceil(hours)} hours needed.")