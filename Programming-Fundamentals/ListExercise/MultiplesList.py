factor = int(input())
counter = int(input())
my_list = []
while len(my_list) != counter:
    if num % factor == 0:
        my_list.append(num)
print(my_list)