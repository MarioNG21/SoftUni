from sys import maxsize
number = int(input())
number_as_string = str(number)
number_as_string_len = len(str(number))
biggest_digit = -maxsize
current_number = 0
for num in range(number_as_string_len):
    new_number = number_as_string[num]
    new_number = current_number
    new_number = int(new_number)
    if new_number > biggest_digit:
        biggest_digit = new_number
    if 