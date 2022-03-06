start_number = int(input())
end_number = int(input())
for number in range(start_number, end_number+1):
    # спец число
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10
    tens_thousands = number // 10000 % 10
    hundred_thousands = number // 100000

    sum_even = tens_thousands + hundreds + units
    sum_odd = hundred_thousands + thousands + tens
    if sum_odd == sum_even:
        print(number, end=" ")