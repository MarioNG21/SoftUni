# въвеждане на n на брой числа
# за всяко едно число -> проверяваме от коя група е и увеличаваме броя с 1
# проценти
#

n = int(input())
count_first = 0
count_second = 0
count_third = 0
count_fourth = 0
count_fifth = 0


for number in range(1, n+1):
    value = int(input())
    if value < 200:
        count_first += 1
    elif 200 <= value <= 399:
        count_second += 1
    elif 400 <= value <= 599:
        count_third += 1
    elif 600 <= value <= 799:
        count_fourth += 1
    elif value >= 800:
        count_fifth += 1

sum_of_all = count_first + count_second + count_third + count_fourth + count_fifth
percent_for_first_group = (count_first / sum_of_all) * 100
percent_for_second_group = (count_second / sum_of_all) * 100
percent_for_third_group = (count_third / sum_of_all) * 100
percent_for_fourth_group = (count_fourth / sum_of_all) * 100
percent_for_fifth_group = (count_fifth / sum_of_all) * 100

print(f"{percent_for_first_group:.2f}%")
print(f"{percent_for_second_group:.2f}%")
print(f"{percent_for_third_group:.2f}%")
print(f"{percent_for_fourth_group:.2f}%")
print(f"{percent_for_fifth_group:.2f}%")