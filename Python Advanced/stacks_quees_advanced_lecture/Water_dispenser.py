from collections import deque

water_qnt = int(input())

people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break

    people_queue.appendleft(command)

while True:
    command = input()
    if command == "End":
        break
    if command.startswith('refill'):
        params = command.split(' ')
        litters_to_add = int(params[1])
        water_qnt += litters_to_add
    else:
        name = people_queue.pop()
        water_wanted = int(command)
        if water_wanted <= water_qnt:
            print(f"{name} got water")
            water_qnt -= water_wanted
        else:
            print(f"{name} must wait ")


print(f"{water_qnt} liters left ")