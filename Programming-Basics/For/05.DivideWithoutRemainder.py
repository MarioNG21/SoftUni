
n = int(input())
count_first = 0
count_second = 0
count_third = 0

for number in range(1, n+1):
    value = int(input())
    if value % 2 == 0:
        count_first += 1
    if value % 3 == 0:
        count_second += 1
    if value % 4 == 0:
        count_third += 1


percent_for_first_group = (count_first / n) * 100
percent_for_second_group = (count_second / n) * 100
percent_for_third_group = (count_third / n) * 100

print(f"{percent_for_first_group:.2f}%")
print(f"{percent_for_second_group:.2f}%")
print(f"{percent_for_third_group:.2f}%")
