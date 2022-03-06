def add_and_subtract(num_1, num_2, num_3):

    def sum_numbers(num_1, num_2):

        return num_1+num_2

    def subtract (sum_of_numbers, num_3):
        subtraction = sum_of_numbers - num_3

        return subtraction

    a = sum_numbers(num_1, num_2)

    return subtract(a, num_3)

number_one = int(input())
number_two = int(input())
number_three = int(input())

print(add_and_subtract(number_one, number_two, number_three))