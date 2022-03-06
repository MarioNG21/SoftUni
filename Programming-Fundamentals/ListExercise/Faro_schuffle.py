card = input().split()
n = int(input())

half_size = len(card) // 2
for j in range(n):
    left_side = card[0:half_size]
    right_side = card[half_size:]

    faro_cards = []

    for i in range(len(left_side)):
        faro_cards.append(left_side[i])
        faro_cards.append(right_side[i])

    card = faro_cards

print(card)