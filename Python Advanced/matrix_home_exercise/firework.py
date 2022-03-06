from collections import deque

fire_works = [int(x) for x in input().split(', ')]
fire_works_deque = deque(fire_works) # first
explosive_power = [int(x) for x in input().split(', ')] # last


palm_fire_work = 0
willow_fire_work = 0
crossette_fire_work = 0


all_collected = False

while True:
    if not fire_works_deque:
        break
    if not explosive_power:
        break

    current_fire_work = fire_works_deque.popleft()
    current_explosive_power = explosive_power.pop()
    if current_fire_work <= 0:
        explosive_power.append(current_explosive_power)
        continue
    if current_explosive_power <= 0:
        fire_works_deque.appendleft(current_fire_work)
        continue

    sum_of_fire = current_fire_work + current_explosive_power

    if sum_of_fire % 3 == 0 and sum_of_fire % 5 == 0:
        crossette_fire_work += 1

    elif sum_of_fire % 3 == 0:
        palm_fire_work += 1

    elif sum_of_fire % 5 == 0:
        willow_fire_work += 1

    else:
        current_fire_work -= 1
        fire_works_deque.append(current_fire_work)
        explosive_power.append(current_explosive_power)

    if palm_fire_work >= 3 and willow_fire_work >= 3 and crossette_fire_work >= 3:
        all_collected = True
        break


if all_collected:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fire_works_deque:
    print(f"Firework Effects left: {', '.join(str(x) for x in fire_works_deque)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm_fire_work}")
print(f"Willow Fireworks: {willow_fire_work}")
print(f"Crossette Fireworks: {crossette_fire_work}")