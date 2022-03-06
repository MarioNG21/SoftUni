def odd_even_sum(num):
    length_of_num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for digit in length_of_num_as_string:
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_sum += digit_int
        else:
            odd_sum += digit_int
    total = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return total
number = int(input())

print(odd_even_sum(number))
