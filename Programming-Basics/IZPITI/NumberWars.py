card_per_player_one = 18
card_per_player_two = 18
name_player_one = input()
name_player_two = input()
command = input()
points_first_player = 0
points_second_player = 0
points_number_war = 0
while command != "End of game":
    card_player_one = int(command)
    card_player_two = int(input())
    if card_player_one > card_player_two:
        points_first = card_player_one - card_player_two
        points_first_player += points_first
    elif card_player_one < card_player_two:
        points_second = card_player_two - card_player_one
        points_second_player += points_second
    else:
        one_more_first_card = int(input())
        one_more_second_card = int(input())
        if one_more_first_card > one_more_second_card:
            points_number_war = points_first_player
            winner = name_player_one
        else:
            points_number_war = points_second_player
            winner = name_player_two
        print("Number wars!")
        print(f"{winner} is winner with {points_number_war} points")
        break
    command = input()
else:
    print(f"{name_player_one} has {points_first_player} points")
    print(f"{name_player_two} has {points_second_player} points")