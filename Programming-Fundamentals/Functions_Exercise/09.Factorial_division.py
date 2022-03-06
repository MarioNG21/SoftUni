import math

 
def factorial_division(num_1: int, num_2: int):
   # multiplication_first = []
   # multiplication_second = []
    result_1 = 1
    result_2 = 1
    for numbers_from_num_1 in range(num_1, 0, -1):
        result_1 = result_1 * numbers_from_num_1
     #   multiplication_first.append(numbers_from_num_1)
    for numbers_from_num_2 in range(num_2, 0, -1):
        result_2 = result_2 * numbers_from_num_2
      #  multiplication_second.append(numbers_from_num_2)
   # product_1 = math.prod(multiplication_first)
   # product_2 = math.prod(multiplication_second)

    return f"{result_1 / result_2:.2f}"


number_1 = int(input())
number_2 = int(input())

print(factorial_division(number_1, number_2))
