# 3 заглавия и останалата част
sold_games = int(input())
wow_game = 0
epic_game = 0
overwatch = 0
others = 0
for game in range(1, sold_games+1):
    name_of_game = input()
    if name_of_game == "Hearthstone":
        wow_game += 1
    elif name_of_game == "Fornite":
        epic_game += 1
    elif name_of_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
wow_game_in_percent = (wow_game / sold_games) * 100
epic_game_in_percent = (epic_game / sold_games) * 100
overwatch_in_percent = (overwatch / sold_games) * 100
others_in_percent = (others / sold_games) * 100
print(f"Hearthstone - {wow_game_in_percent:.2f}%")
print(f"Fornite - {epic_game_in_percent:.2f}%")
print(f"Overwatch - {overwatch_in_percent:.2f}%")
print(f"Others - {others_in_percent:.2f}%")