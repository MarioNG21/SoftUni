eggs_player_one = int(input())
eggs_player_two = int(input())
command = input()
first_player = 0
second_player = 0
while command != "End of battle":
    winner = command
    if winner == "one":
        first_player += 1
        eggs_player_two -= 1
    else:
        second_player += 1
        eggs_player_one -= 1
    if eggs_player_one == 0 or eggs_player_two == 0:
        if eggs_player_one == 0:
            print(f"Player one is out of eggs. Player two has {eggs_player_two} eggs left.")
        else:
            print(f"Player two is out of eggs. Player one has {eggs_player_one} eggs left.")
        break
    command = input()
else:
    print(f"Player one has {eggs_player_one} eggs left.")
    print(f"Player two has {eggs_player_two} eggs left.")