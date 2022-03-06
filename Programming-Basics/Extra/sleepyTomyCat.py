# нормата за игра на том е 30 000 минути в година
# времето за игра зависи от свободните дни
# Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# Когато почива, стопанинът му си играе с него  по 127 минути на ден.
#
#
#
#
#
#
norm = 30000
rest_days = int(input())
work_days = 365 - rest_days
play_time = (work_days * 63 + rest_days * 127)

if play_time > norm :
    print(f"Tom will run away")
    rest = play_time - norm
    play_time_in_hours = rest // 60
    play_time_in_minutes = rest % 60
    print(f"{play_time_in_hours} hours and {play_time_in_minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    rest = norm - play_time
    play_time_in_hours = rest // 60
    play_time_in_minutes = rest % 60
    print(f"{play_time_in_hours} hours and {play_time_in_minutes} minutes less for play")



