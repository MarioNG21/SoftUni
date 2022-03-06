football_club = input()
played_matches = int(input())
if played_matches < 1:
    print(f"{football_club} hasn't played any games during this season.")
else:
    points = 0
    win_counter = 0
    draw_counter = 0
    lose_counter = 0
    for match in range(1, played_matches+1):
        result = input()
        if result == "W":
            points += 3
            win_counter += 1
        elif result == "D":
            points += 1
            draw_counter += 1
        elif result == "L":
            points += 0
            lose_counter += 1
    print(f"{football_club} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {draw_counter}")
    print(f"## L: {lose_counter}")
    print(f"Win rate: {((win_counter / played_matches)*100):.2f}%")
