first_command = input()
overall_won = 0
overall_loses = 0
overall_matches = 0
while first_command != "End of tournaments":
    name_of_tournament = first_command
    played_matches_for_one = int(input())
    won_matches = 0
    lost_matches = 0
    for matches in range(1, played_matches_for_one+1):
        Desi_team_points = int(input())
        other_side_points = int(input())
        if Desi_team_points > other_side_points:
            diff = Desi_team_points - other_side_points
            won_matches += 1
            print(f"Game {matches} of tournament {name_of_tournament}: win with {diff} points.")
        else:
            lost_points = other_side_points - Desi_team_points
            lost_matches += 1
            print(f"Game {matches} of tournament {name_of_tournament}: lost with {lost_points} points.")
    overall_won += won_matches
    overall_loses += lost_matches
    overall_matches += (won_matches+lost_matches)
    first_command = input()
else:
    won_matches_in_percent = (overall_won / overall_matches) * 100
    lost_matches_in_percent = (overall_loses / overall_matches) * 100
    print(f"{won_matches_in_percent:.2f}% matches win")
    print(f"{lost_matches_in_percent:.2f}% matches lost")