team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_input = input().split()

terminated = False
for cards in cards_input:
    card_info = cards.split("-")

    team_name = card_info[0]
    player_number = int(card_info[1])

    if team_name == "A" and player_number in team_A:
        team_A.remove(player_number)
    elif team_name == "B" and player_number in team_B:
        team_B.remove(player_number)

    if len(team_A) < 7 or len(team_B) < 7:
        terminated = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated:
    print(f"Game was terminated")

