from collections import deque

cups_cap = [int(x) for x in input().split()]
bottles_cap = [int(x) for x in input().split()]

cups_queue = deque()

for cup in cups_cap:
    cups_queue.append(cup)

wasted_water = 0

while True:
    current_cup = cups_queue[0]
    current_bottle = bottles_cap[-1]
    if current_bottle > current_cup:
        wasted = current_bottle - current_cup
        wasted_water += wasted
        bottles_cap.pop()
        cups_queue.popleft()
    else:
        for bottle in bottles_cap[::-1]:
            if bottle > current_cup:
                wasted_water += bottle - current_cup
                cups_queue.popleft()
                bottles_cap.pop()
                current_cup -= bottle
                if current_cup <= 0:
                    break
            else:
                current_cup -= bottle
                bottles_cap.pop()
                if current_cup <= 0:
                    cups_queue.popleft()
                    break
    if not cups_queue:
        bottles_cap_str = [str(x) for x in bottles_cap]
        print(f"Bottles: {' '.join(bottles_cap_str)}")
        break
    elif not bottles_cap:
        cups_str = [str(x) for x in cups_queue]
        print(f"Cups: {' '.join(cups_str)}")
        break

print(f"Wasted litters of water: {wasted_water}")