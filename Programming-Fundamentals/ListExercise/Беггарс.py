numbers = input().split(", ")

new_list = []

for num in numbers:
    number = int(num)
    new_list.append(number)

for ch in range(len(new_list)):
    new_num = new_list[ch]
    if new_num == 0:
        new_list.remove(0)
        new_list.append(new_num)


print(new_list)

