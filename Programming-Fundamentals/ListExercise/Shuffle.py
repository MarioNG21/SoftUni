cards = input().split(" ")
number_of_shuffles = int(input())

half_size = int(len(cards) / 2)

for j in range(number_of_shuffles):
    left_part = cards[0:half_size]
    right_part = cards[half_size:]

    faro_cards = []

    for i in range(len(left_part)):
        faro_cards.append(left_part[i])
        faro_cards.append(right_part[i])

    cards = faro_cards

print(cards)