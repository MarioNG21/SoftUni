from collections import deque

chocolates = deque([int(x) for x in input().split(', ')])
cups_of_milk = deque([int(x) for x in input().split(', ')])

counter = 0

while cups_of_milk and chocolates:
    if chocolates[-1] <= 0 or cups_of_milk[0] <= 0:
        if chocolates[-1] <= 0:
            chocolates.pop()
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
        continue
    chocolate = chocolates.pop()
    cup = cups_of_milk.popleft()

    if chocolate == cup:
        counter += 1

    else:
        cups_of_milk.append(cup)
        chocolates.append(chocolate - 5)

    if counter >= 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break
else:
    print("Not enough milkshakes.")


if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
