def is_palindrome(collection: list):
    reversed_collection = collection[::-1]
    if reversed_collection == collection:
        return True
    else:
        return False





positive_nums = [int(num) for num in input().split(", ")]

while len(positive_nums) > 0:
    for numbers in positive_nums:
        numbers_str = str(numbers)
        new_list = []
        for el in range(len(numbers_str)):
            num_int = int(numbers_str[el])
            new_list.append(num_int)
        print(is_palindrome(new_list))
    break


