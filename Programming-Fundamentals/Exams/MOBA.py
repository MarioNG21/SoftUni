command = input()
player_pool = {}


while not command == 'Season end':
    if '->' in command:
        cmd_arg = command.split(' -> ')
        player = cmd_arg[0]
        position = cmd_arg[1]
        skill = int(cmd_arg[2])
        if player not in player_pool:
            player_pool[player] = {position: skill}
        elif position not in player_pool[player]:
            player_pool[player].update({position: skill})
        else:
            if player_pool[player][position] < skill:
                player_pool[player][position] = skill

    elif 'vs' in command:
        cmd_arg = command.split(' vs ')
        p_1 = cmd_arg[0]
        p_2 = cmd_arg[1]
        if p_1 in player_pool and p_2 in player_pool:
            p_1_position = list(player_pool[p_1].keys())
            p_2_position = list(player_pool[p_2].keys())
            p_1_dies = False
            p_2_dies = False
            for j in range(len(p_2_position)):
                i = p_2_position[j]
                if i in p_1_position:
                    dmg_1 = player_pool[p_1][i]
                    dmg_2 = player_pool[p_2][i]
                    if dmg_1 > dmg_2:
                        p_2_dies = True
                        continue
                    else:
                        p_1_dies = True
                        continue
            if p_1_dies:
                del player_pool[p_1]
            if p_2_dies:
                del player_pool[p_2]

    command = input()
a = 5
new_dict = {}
for i, j in player_pool.items():
    if i not in new_dict:
        new_dict[i] = 0
    new_dict[i] += sum(j.values())

for player, items in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {items} skill")
    for p, s in sorted(player_pool[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {p} <::> {s}")

