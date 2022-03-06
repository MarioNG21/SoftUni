
def the_smallest_num(num_1: int, num_2: int, num_3: int):
    if num_1 < num_2 < num_3:
        return num_1
    elif num_2 < num_1 < num_3:
        return num_2
    elif num_3 < num_2 < num_1:
        return num_3


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(the_smallest_num(number_1, number_2, number_3))