number = int(input())
all_number = 2 * number
sum_left = 0
sum_right = 0
for numbers in range(1, number+1):
    value = int(input())
    sum_left += value
for numbers in range(number+1, all_number+1):
    value_right = int(input())
    sum_right += value_right

if sum_left == sum_right:
    print(f"Yes, sum = {sum_right}")
else:
    diff= abs(sum_left-sum_right)
    print(f"No, diff = {diff}")