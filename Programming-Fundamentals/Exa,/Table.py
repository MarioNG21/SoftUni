ch = input().split(', ')
new_dict = {}
for el in range(len(ch)):
    character = ch[el]
    if character not in new_dict:
        new_dict[character] = ord(character)

print(new_dict)