current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    happy_year = True
    for test_position in range(len(current_year_as_string)):
        test_digit = current_year_as_string[test_position]
        for current_position in range(len(current_year_as_string)):
            if test_digit == current_year_as_string[current_position] and test_position != current_position:
                happy_year = False
                break
    if happy_year:
        print(current_year)
        break