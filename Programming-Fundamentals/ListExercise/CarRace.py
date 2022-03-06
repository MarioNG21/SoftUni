list_numbers = [int(num) for num in input().split()]

finish_line_index = int(len(list_numbers) / 2)
finish_line_num = list_numbers[finish_line_index]

if len(list_numbers) % 2 == 0:
    exit()

first_racer = list_numbers[:finish_line_index]
second_racer = list_numbers[finish_line_index+1:]
second_racer_reversed = second_racer[::-1]
sum_first = 0
sum_second = 0

for first_el in first_racer:
    time = first_el
    if time == 0:
        reduced_time = sum_first * 0.2
        sum_first -= reduced_time

    sum_first += time

for second_el in second_racer_reversed:
    time_2 = second_el
    if time_2 == 0:
        reduced_time = sum_second * 0.2
        sum_second -= reduced_time

    sum_second += time_2


if sum_first < sum_second:
    winner = "left"
    print(f"The winner is {winner} with total time: {sum_first:.1f}")

elif sum_second < sum_first:
    winner = "right"
    print(f"The winner is {winner} with total time: {sum_second:.1f}")
