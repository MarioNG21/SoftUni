str_integers = input().split(", ")
counter = int(input())
sum_of_each_beggar = []
start_index = 0
for beggar in range(1, counter+1):
    current_sum = 0
    for sum in range(start_index, len(str_integers), counter):
        current_sum += int(str_integers[sum])
    sum_of_each_beggar.append(current_sum)
    start_index += 1
print(sum_of_each_beggar)
