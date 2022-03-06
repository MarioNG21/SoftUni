command = input()
battle_dict = {}
while not command == "Results":
    cmd_arg = command.split(":")
    action = cmd_arg[0]
    if action == "Add":
        name = cmd_arg[1]
        health = int(cmd_arg[2])
        energy = int(cmd_arg[3])
        if name not in battle_dict:
            battle_dict[name] = {"Health": health, "Energy": energy}
        elif name in battle_dict:
            battle_dict[name]["Health"] += health
    elif action == "Attack":
        attacker = cmd_arg[1]
        defender = cmd_arg[2]
        damage = int(cmd_arg[3])
        if attacker in battle_dict and defender in battle_dict:
            battle_dict[defender]["Health"] -= damage
            battle_dict[attacker]["Energy"] -= 1
            if battle_dict[defender]["Health"] <= 0:
                print(f"{defender} was disqualified!")
                del battle_dict[defender]
            if battle_dict[attacker]["Energy"] <= 0:
                print(f"{attacker} was disqualified!")
                del battle_dict[attacker]
    elif action == "Delete":
        username = cmd_arg[1]
        if username == "All":
            del battle_dict
            battle_dict = {}
        else:
            del battle_dict[username]
    command = input()
if battle_dict != {}:
    print(f"People count: {len(battle_dict)}")
    for n, values in sorted(battle_dict.items(), key=lambda kvp: (-kvp[1]["Health"], kvp[0])):
        print(f"{n} - {values['Health']} - {values['Energy']}")

