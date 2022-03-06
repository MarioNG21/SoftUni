# до получаване на командата стоп
# при победа на една игра +20
# на края на деня се изчислява стойността на печалбата
# ако спечелените пари са повече от загубените -> победители за деня
# победител на деня -> печалбата за деня скача с 10 процента
# победител на турнира -> печалбата до сега се увеличава с 20 процента
# нямаме равен брой спечелени игри и загубени
days_for_tournament = int(input())
overall_sum = 0
overall_wins = 0
overall_lose = 0
have_won = False
for days in range(1, days_for_tournament+1):
    command = input()
    sum_for_the_day = 0
    win_counter = 0
    lose_counter = 0
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            sum_for_the_day += 20
            win_counter += 1
        else:
            lose_counter += 1
        command = input()
    if win_counter > lose_counter:
        sum_for_the_day = sum_for_the_day + 0.1 * sum_for_the_day
    overall_wins += win_counter
    overall_lose += lose_counter
    overall_sum += sum_for_the_day
if overall_wins > overall_lose:
    have_won = True
    overall_sum = overall_sum + 0.2 * overall_sum


if have_won:
    print(f"You won the tournament! Total raised money: {overall_sum:.2f}")
elif not have_won:
    print(f"You lost the tournament! Total raised money: {overall_sum:.2f}")