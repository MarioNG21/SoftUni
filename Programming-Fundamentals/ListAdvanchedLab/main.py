num_list = [int(el) for el in input().split(", ")]

print([index for index in range(len(num_list)) if num_list[index] % 2 == 0])