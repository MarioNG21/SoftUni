def is_registered(parking_dict: dict, name: str, plate: str):
    if name not in parking_dict:
        parking_lot_dict[name] = plate
        print(f"{name} registered {plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {plate}")

    return parking_dict


def is_unregistered(parking_dict: dict, name: str):
    if name not in parking_dict:
        print(f"ERROR: user {name} not found")
    else:
        print(f"{name} unregistered successfully")
        parking_dict.pop(name)
    return parking_dict


parking_lot_dict = {}
number_of_registers = int(input())

for _ in range(0, number_of_registers):
    cmd_arg = input().split()
    type_action = cmd_arg[0]
    if type_action == "register":
        username = cmd_arg[1]
        plate_num = cmd_arg[2]
        is_registered(parking_lot_dict, username, plate_num)
    elif type_action == "unregister":
        username_unreg = cmd_arg[1]
        is_unregistered(parking_lot_dict, username_unreg)


for key, value in parking_lot_dict.items():
    print(f"{key} => {value}")