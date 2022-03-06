dragon_dict = {}
number_of_dragons = int(input())
dict_with_average_score = {}
counter = 0
for i in range(number_of_dragons):
    command = input().split()
    type_of_dragon = command[0]
    name = command[1]
    dmg = (command[2])
    if dmg == 'null':
        dmg = 45
    health = (command[3])
    if health == 'null':
        health = 250
    armor = (command[4])
    if armor == 'null':
        armor = 10
    if type_of_dragon not in dragon_dict:
        dragon_dict[type_of_dragon] = {name: [int(dmg), int(health), int(armor)]}
    else:
        dragon_dict[type_of_dragon][name] = [int(dmg), int(health), int(armor)]

    # elif name not in dragon_dict[type_of_dragon]:
    #    dragon_dict[type_of_dragon].update({name: [int(dmg), int(health), int(armor)]})
    # else:
    #     dragon_dict[type_of_dragon] = ({name: [int(dmg), int(health), int(armor)]})
average_dict = {}

for colour, item in dragon_dict.items():
    sum_health = 0
    sum_dmg = 0
    sum_armor = 0
    for n, stats in item.items():
        sum_dmg += stats[0]
        sum_health += stats[1]
        sum_armor += stats[2]
    average_dict[colour] = [(sum_dmg / len(item)), sum_health / len(item), sum_armor / len(item)]

for t, value in dragon_dict.items():
    print(f"{t}::({average_dict[t][0]:.2f}/{average_dict[t][1]:.2f}/{average_dict[t][2]:.2f})")
    for n, double in sorted(value.items(), key=lambda kvp: kvp[0]):
        print(f"-{n} -> damage: {double[0]}, health: {double[1]}, armor: {double[2]}")