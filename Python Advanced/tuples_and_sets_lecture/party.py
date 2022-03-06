counter = int(input())

soft_uni = {input() for _ in range(counter)}
counter = 0
while True:
    command = input()
    if command == "END":
        break
    soft_uni.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in soft_uni if is_vip(g)])
regular = sorted([g for g in soft_uni if g not in vip_guests])
print(len(soft_uni))
[print(g) for g in vip_guests]
[print(g) for g in regular]
