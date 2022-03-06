import re
demon_book = {}
demons = input().split(', ')
pattern_health = r'([A-Za-z](^|$(\+\-\*\/))?)'
pattern_damage = r'([+-]?[0-9]+(\.[0-9]+)?'
pattern_end = r'(\*+|\/+)'

for demon in demons:
    sum_of_health = 0
    sum_damage = 0
    matches_health = re.finditer(pattern_health, demon)

    for word in matches_health:
        sum_of_health += ord(word.group())

    matches_damage = re.finditer(pattern_damage, demon)

    for match in matches_damage:
        damage = (match.group())
        if '-' in damage:
            sum_damage += float(damage)
        else:
            sum_damage += float(damage)
    match_action = re.finditer(pattern_end, demon)
    for end in match_action:
        action = end.group()
        for i in action:
            if i == '*':
                sum_damage *= 2
            elif i == '/':
                sum_damage /= 2

    demon_name = ''.join(demon)
    demon_book[demon_name] = {'health': sum_of_health, 'damage': sum_damage}

sorted_demons_by_name = sorted(demon_book.items(), key=lambda kvp: kvp[0])

for key, value in sorted_demons_by_name:
    print(f"{key} - {value['health']} health, {value['damage']:.2f} damage")