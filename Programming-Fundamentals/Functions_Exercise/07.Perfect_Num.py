def is_perfect_num(num: int):
    sum_of_nums = num
    for el in range(1, num):
        if num % el == 0:
            sum_of_nums += el
    if sum_of_nums / 2 == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_num(number))
