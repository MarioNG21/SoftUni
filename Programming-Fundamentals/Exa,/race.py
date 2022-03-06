import re
participants = input().split(', ')
command = input()
date = {}
while command != "end of race":
    patter_name = r'(?P<name>[A-Za-z0-9])'
    match_name = re.finditer(patter_name, command)
    participants_name = []
    sum_of_distance = 0
    for name in match_name:
        new_name = name.group()
        if new_name.isalpha():
            participants_name.append(new_name)
        elif new_name.isdigit():
            sum_of_distance += int(new_name)
    participants_name = ''.join(participants_name)
    if participants_name in participants:
        if participants_name not in date:
            date[participants_name] = sum_of_distance
        else:
            date[participants_name] += sum_of_distance
    command = input()
sorted_list = sorted(date.items(), key=lambda kvp: -kvp[1])
print(f"1st place: {sorted_list[0][0]}")
print(f"2nd place: {sorted_list[1][0]}")
print(f'3rd place: {sorted_list[2][0]}')

