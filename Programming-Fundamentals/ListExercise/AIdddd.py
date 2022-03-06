number_of_people = [int(num) for num in input().split()]
counter = int(input())
killed_list = []
position_counter = 1
while True:
    for el in range(0, len(number_of_people)):
        possible_kill = number_of_people[el]
        if position_counter == counter:
            killed_one = possible_kill
            killed_list.append(killed_one)
            number_of_people[el] = 0
            position_counter = 1
        else:
            position_counter += 1
    for number in number_of_people:
        number_int = int(number)
        if number_int == 0:
            number_of_people.remove(0)
    if len(number_of_people) == 0:
        break

new_list = ""
for el in killed_list:
    new_number_Str = str(el)
    new_list += new_number_Str

print(f"[{','.join(new_list)}]")