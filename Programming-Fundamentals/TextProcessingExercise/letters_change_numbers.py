game_string = input().split()

sum_1 = 0
sum_2 = 0
for double in game_string:
    if double[0].isupper():
        list_1 = []
        word = double[0]
        asci = (ord(word) - 65) + 1
        for i in range(1, len(double)-1):
            digit = double[i]
            list_1.append(digit)
        new_num = int(''.join(list_1))
        first_op = new_num / asci
        if double[len(double)-1].isupper():
            word_two = double[len(double)-1]
            position = (ord(word_two) - 65) + 1
            second_op = first_op - position
            sum_1 += second_op
        else:
            word_two = double[len(double)-1]
            position = (ord(word_two) - 97) + 1
            second_op = first_op + position
            sum_1 += second_op
    else:
        list_2 = []
        word = double[0]
        asci = (ord(word) - 97) + 1
        for i in range(1, len(double) - 1):
            digit = double[i]
            list_2.append(digit)
        new_num = int(''.join(list_2))
        first_op = new_num * asci
        if double[len(double)-1].isupper():
            word_two = double[len(double)-1]
            position = (ord(word_two) - 65) + 1
            second_op = first_op - position
            sum_2 += second_op
        else:
            word_two = double[len(double)-1]
            position = (ord(word_two) - 97) + 1
            second_op = first_op + position
            sum_2 += second_op

print(f"{sum_1+sum_2:.2f}")