number = int(input())
num_as_string = ""
for num in range(1, number+1):
    num_as_string = str(num)
    sum_digit = 0
    for symbol in num_as_string :
       sum_digit += int(symbol)
    if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
        num_special = True
    else:
        num_special = False
    print(f"{num} -> {num_special}")
