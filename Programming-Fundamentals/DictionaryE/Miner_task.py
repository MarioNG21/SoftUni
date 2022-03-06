command = input()
counter = 1

resource_dict = {}
new_one = ""
while command != "stop":
    if counter % 2 == 1:
        resource = command
        new_one = resource
        if new_one not in resource_dict:
            resource_dict[resource] = 0
    elif counter % 2 == 0:
        quantity = int(command)
        if new_one in resource_dict:
            resource_dict[new_one] += quantity

    counter += 1
    command = input()

for Resources, qnt in resource_dict.items():
    print(f"{Resources} -> {qnt}")