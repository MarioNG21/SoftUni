number = int(input())
plant_dict = {}
for i in range(number):
    cmd = input().split("<->")
    name = cmd[0]
    rarity = int(cmd[1])
    if name not in plant_dict:
        plant_dict[name] = {"Rarity": rarity, "Rating": []}
    else:
        plant_dict[name]["Rarity"] = rarity
command = input()

while not command == "Exhibition":
    cmd_arg = command.split(": ")
    action = cmd_arg[0]
    if action == "Rate":
        new_command = cmd_arg[1].split(" - ")
        plant_name = new_command[0]
        if plant_name in plant_dict:
            rating = int(new_command[1])
            plant_dict[plant_name]["Rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        update_command = cmd_arg[1].split(" - ")
        plant = update_command[0]
        new_rarity = int(update_command[1])
        if plant in plant_dict:
            plant_dict[plant]["Rarity"] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        reset_name = cmd_arg[1]
        if reset_name in plant_dict:
            plant_dict[reset_name]["Rating"].clear()
        else:
            print("error")

    command = input()
for name, items in plant_dict.items():
    average_sum = 0
    if  items["Rating"] == []:
        items["Rating"] = [0]
    for i in items["Rating"]:
        average_sum += i
    sum_rating = average_sum / len(items["Rating"])
    plant_dict[name] = {"Rarity": items["Rarity"], "Average": sum_rating}

print("Plants for the exhibition:")
for plants, new_items in sorted(plant_dict.items(), key=lambda kvp: (-kvp[1]["Rarity"], -kvp[1]["Average"])):
    print(f"- {plants}; Rarity: {new_items['Rarity']}; Rating: {new_items['Average']:.2f}")