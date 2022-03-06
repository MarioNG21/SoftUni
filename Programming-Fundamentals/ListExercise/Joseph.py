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
            number_of_people.remove(killed_one)
            position_counter = 1
        else:
            position_counter += 1

    if len(number_of_people) == 0:
        break
