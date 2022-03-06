sequence_1 = input().split(", ")
sequence_2 = input().split(", ")
new_list = []
for el in sequence_1:
    el_as_string = " ".join(el)
    for el_2 in sequence_2:
        el_as_string_2 = " ".join(el_2)
        if el_as_string in el_as_string_2:
            new_list.append(el)
            break

print(new_list)