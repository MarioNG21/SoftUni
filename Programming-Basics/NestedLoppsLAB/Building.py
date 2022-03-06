count_floors = int(input())
count_rooms = int(input())
for floor in range(count_floors, 0, -1):
    for rooms in range(0, count_rooms):
        if floor == count_floors:
            print(f"L{floor}{rooms}", end = " ")
        elif floor % 2 != 0:
            print(f"A{floor}{rooms}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{rooms}", end=" ")
    print()

